import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

from pathlib import Path

if __name__ == '__main__':

    # Charger les données
    chemin_base = Path(__file__).parent
    chemin_bitcoin = chemin_base.parent.joinpath("data", "crypto", "bitcoin.csv")

    df = pd.read_csv(chemin_bitcoin)

    # Afficher les 5 premières lignes
    print(df.head())

    # Utiliser la date comme index (transformation)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)


    # Calculer la moyenne mobile de 30 jours
    df['MM30'] = df['Close'].rolling(window=30).mean()

    # Produire un graphique de la moyenne mobile de 30 jours
    plt.figure(figsize=(14,7))
    plt.plot(df['Close'], label='Fermeture')
    plt.plot(df['MM30'], label='Moyenne mobile 30 jours', color='orange')

    # Paramétrer le texte de l'axe des x
    localisateur = mdates.YearLocator() # Trouver les années
    formatter = mdates.DateFormatter('%Y-%m-%d') # Formater les années

    plt.gca().xaxis.set_major_locator(localisateur)
    plt.gca().xaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45)


    plt.xlabel('Date')
    plt.ylabel('Prix de fermeture en USD')
    plt.title('Moyenne mobile de 30 jours du Bitcoin à la fermeture')

    plt.legend(loc='best')
    plt.show()