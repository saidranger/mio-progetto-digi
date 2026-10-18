paragrafo1 = '''
Consiglio sempre di installare l'ultima versione del Digiproject,soprattutto perché è sempre compatibile con le vecchie versioni.
Anche perchè il 99% delle volte ci troveremo ad installare il **Digiproject partendo da una configurazione** quanto più possibile **adatta al cliente.** 
Nello specifico mi riferisco al fatto che avremmo un file **digiproject.db** (recuperato da un'altra istallazione) adatto per quel cliente che andremmo a copiare nella nuova istallazione.

Spiegherò passo passo come installarlo.
Un occhita al necessario :hammer_and_wrench:
- **DIGIproject.Server.Setup.2.182.2.3852.exe** (ad oggi questa è l'ultima versione).
- il **digiproject.db** già configurato preso da un'altra installazione.
>   Consiglio:
>
>   Recuperare un digiproject.db da un cliente, è sufficente scaricare uno dei backup che si trovano nella cartella c:\\digi\\backup '''

paragrafo2 = '''
Se si dispone solamente del setup **"DIGIproject.Server.Setup.xxxx.exe"** è sufficente cliccare con il tasto destro del mouse sul file e selezionare l'opzione **"Esegui come amministratore".**
Al termine verrà installato anche il servizio di Windows **"DigiProject Server"** che su documentazione ufficiale dice che sarà **"avviato automaticamente"**, 
invece vi consiglio sempre di controllare se è realmente avviato e se non lo è avviatelo a mano, inoltre spesso mi è capitato che lo stesso non si avviava, in questo caso riavviate il PC e avviatelo a mano.
Nella cartella **C:\\Program Files(x86)\\DIGI\\DIGIproject Server** troverete il file **DigiProject.Client.setup.exe**, questo serve per installare il client che potra essere installato su qualsiasi PC della rete, anche se non è presente il server, infatti il client si collegherà al server tramite la rete locale.

Una volta installato il client, all'avvio dovete inserire:
  - username *admin*
  - password *admin*\n
successivamente vi chiederà di inserire la chiave di licenza.
Date un'occhiata alle immagini qui sotto.
'''
paragrafo3 = '''
Il Digiproject.db prelevato da un'altra installazione contiene al suo interno tutte le configurazioni per inizializzare le Librerie, i Reparti, i Testi, ecc..\n
ma contiene anche le pesate, i plu, i lotti, lo storico degli errori e delle comunicazioni da e verso le bilance, lo storico delle importazioni di variazioni, ecc..\n
quest'ultimi non ci servono e potrebbero andare in conflitto con il sistema!\n
Quindi prima di copiare questo database, lo stesso deve essere pulito da tutti i dati che non ci servono.\n
La pulizia del database si ottiene utilizzando un programmino **"DIGIproject_DB_Maintenance-exe"**, da non confondere con "ToDIGIprj_DB_Maintenance.exe", si trova nella cartella ToDigiPrj che di solito è situata in **c:\\Digi\\ToDigiPrj**.\n
*Di seguito uno screenshot delle opzini da selezionare per ripulire il Database.*'''