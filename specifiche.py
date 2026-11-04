import json
from json import JSONDecodeError
from pathlib import Path

import streamlit as st


DATA_PATH = Path(__file__).resolve().parent / "static" / "Spec" / "specifiche-data.json"
LABELS = {
    "Min": "Minimo",
    "Max": "Massimo",
    "ItemCount": "Numero opzioni",
    "Decimal": "Decimali",
    "Base": "Base",
    "Max2": "Massimo 2",
    "SpecCount": "Numero specifiche",
    "StartIndex": "Indice iniziale",
    "SubType": "Sottotipo",
}


@st.cache_data(show_spinner=False)
def load_documents():
    try:
        with DATA_PATH.open(encoding="utf-8") as data_file:
            return json.load(data_file)
    except OSError as exc:
        raise RuntimeError(
            f"Impossibile leggere il file delle specifiche: {DATA_PATH}"
        ) from exc
    except JSONDecodeError as exc:
        raise RuntimeError(
            f"Il file delle specifiche non contiene JSON valido: {DATA_PATH}"
        ) from exc


def searchable_text(document, record):
    parts = [
        document["file"],
        record.get("id", ""),
        record.get("title", ""),
        record.get("sourceTitle", ""),
    ]
    parts.extend(
        value
        for item in record.get("items", [])
        for value in (item.get("it", ""), item.get("value", ""))
    )
    parts.extend(
        str(value)
        for pair in record.get("fields", {}).items()
        for value in pair
    )
    return " ".join(parts).casefold()


def render_record(record, show_raw):
    with st.container(border=True):
        st.markdown(f"**{record.get('id', '')}**")
        st.markdown(record.get("title") or "Voce senza descrizione")
        if record.get("sourceTitle"):
            st.caption(record["sourceTitle"])

        fields = record.get("fields", {})
        limits = [
            f"**{LABELS.get(key, key)}:** {value}"
            for key, value in fields.items()
            if key in ("Min", "Max")
        ]
        if limits:
            st.markdown(" · ".join(limits))

        items = record.get("items", [])
        if items:
            st.markdown(
                "\n".join(
                    f"- **{item.get('key', '').removeprefix('Item')}:** "
                    f"{item.get('it') or item.get('value', '')}"
                    for item in items
                )
            )

        raw = record.get("raw")
        if raw and show_raw:
            st.code(raw, language="ini")


def main():
    if not st.session_state.get("user_logged_in"):
        st.error("Il contenuto è privato: effettua il login per accedere.")
        if st.button("Fai il login", icon="🔑", type="primary"):
            st.switch_page("login.py")
        return

    st.title("Specifiche di configurazione per SM-5300x e SM-6000")
    st.caption("Documentazione tecnica in italiano, organizzata per documento e parametro.")

    try:
        documents = load_documents()
    except RuntimeError as exc:
        st.error(str(exc))
        st.stop()

    parameter_count = sum(len(document["records"]) for document in documents)
    metric_docs, metric_parameters = st.columns(2)
    metric_docs.metric("Documenti", len(documents))
    metric_parameters.metric("Parametri", parameter_count)

    query = st.text_input(
        "Cerca nelle specifiche",
        placeholder="Codice, descrizione o valore (es. 140A001)",
    ).strip().casefold()
    file_options = ["Tutti i documenti"] + [
        document["file"] for document in documents
    ]
    selected_file = st.selectbox("Documento", file_options)
    show_raw = st.checkbox("Mostra i dati originali dei file .des")

    if selected_file == "Tutti i documenti" and not query:
        st.info("Seleziona un documento oppure cerca un parametro.")
        return

    result_count = 0
    for document in documents:
        if selected_file != "Tutti i documenti" and document["file"] != selected_file:
            continue

        records = [
            record
            for record in document["records"]
            if not query or query in searchable_text(document, record)
        ]
        if not records:
            continue

        result_count += len(records)
        with st.expander(
            f"{document['file']} · {len(records)} parametri",
            expanded=bool(query),
        ):
            main_info = document.get("main", {})
            if main_info:
                details = " · ".join(
                    f"{LABELS.get(key, key)}: {value}"
                    for key, value in main_info.items()
                )
                st.caption(f"Intestazione documento — {details}")

            for record in records:
                render_record(record, show_raw)

    if query:
        st.caption(
            f"{result_count} "
            f"{'risultato' if result_count == 1 else 'risultati'}"
        )
        if not result_count:
            st.info("Nessun parametro corrisponde alla ricerca.")


main()
