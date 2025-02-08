#   Dataevento    Sito                       Classe          Servizio   Apparato  Disservizio             Descrizione  Gravita
#   01/01/2023 10:42    _[...]    IMPIANTI DVB-T    MUX-R10    TXB    TS Su Carico Artificiale    on    Warning
#   01/01/2023 10:42    _[...]    IMPIANTI DVB-T    MUX-R10    TXB    TC Accensione              riposo    Clear

from matplotlib import pyplot as plt
import pandas as pd  # Importa la libreria pandas con l'alias 'pd'

# Importa il CSV
percorso = r"C:\Users\p407589\Documents\_GGL\Python\Pandas\_AgrigentoGiache.csv"  # Percorso del file CSV
data = pd.read_csv(percorso, sep=';', encoding='utf-8', header=0)  # Legge il file CSV specificando il separatore ';' e l'encoding 'utf-8', impostando l'intestazione alla riga 0

# Converti la colonna 'Dataevento' in formato datetime
data['Dataevento'] = pd.to_datetime(data['Dataevento'], format='%d/%m/%Y %H:%M')  # Converte la colonna 'Dataevento' nel formato datetime specificato '%d/%m/%Y %H:%M'

# Seleziono solo quello che mi interessa
data = data.loc[data['Apparato'].isin(['TXA', 'TXB', 'PILOTA A', 'PILOTA B', 'VIRTUALE', 'TX1']) & ((data['Servizio'] == 'MUX-R10'))]  # Filtra i dati selezionando solo quelli con valori specifici nelle colonne 'Apparato' e 'Servizio'

# Ordino 
#data = data.sort_values('Dataevento')
data = data.sort_index()  # Ordina i dati per indice

# inizializzo lista
pattern = []  # Inizializza una lista vuota per contenere i pattern

# Conto quello che è successo nelle precedenti dal TSV disservizio
for i in range(1, len(data)):  # Itera attraverso le righe del DataFrame a partire dalla seconda riga
    if data.iloc[i]['Disservizio'] == 'TSV Disservizio' and data.iloc[i]['Descrizione'] == 'ON':  #Cerca l'inizio del disservizio
        print(f"- {data.iloc[i]['Dataevento']} - {data.iloc[i]['Apparato']} - {data.iloc[i]['Servizio']} - {data.iloc[i]['Descrizione']}")  # Stampa le informazioni sul disservizio

        # Ottieni le righe precedenti per l'analisi
        righe_precedenti = data.iloc[i-5:i]  # qui stabilisco quante righe prima devo analizzare

        # Calcola il conteggio delle occorrenze di ciascun valore nella colonna "Disservizio"
        conteggio_punti = righe_precedenti['Disservizio'].value_counts()  # Conta le occorrenze dei disservizi nelle righe precedenti

        # Aggiungi il conteggio alla lista dei pattern
        pattern.append(conteggio_punti)  # Aggiunge il conteggio alla lista dei pattern

# Concatena tutti i conteggi dei pattern in un unico DataFrame
pattern_df = pd.concat(pattern, axis=1)  # Concatena i conteggi dei pattern in un unico DataFrame
pattern_df.fillna(0, inplace=True)  # Sostituisci i valori NaN con 0

# Somma tutte le occorrenze degli stessi punti in tutte le colonne
pattern_df_sum = pattern_df.sum(axis=1)  # Calcola la somma delle occorrenze di ciascun punto su tutte le colonne
pattern_df_sum = pattern_df_sum.sort_values(ascending=False)

# Stampa il DataFrame con la somma delle occorrenze
print(pattern_df_sum)  # Stampa il DataFrame con la somma delle occorrenze dei disservizi

# Plot
plt.figure(figsize=(10, 6))
pattern_df_sum.plot(kind='bar')
plt.title('Conteggio degli eventi accaduti 1 minuto prima il disservizio')
plt.xlabel('Apparato/Servizio')
plt.ylabel('Numero')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
