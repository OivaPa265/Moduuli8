import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='sinun salasanasi',
    autocommit=True
    )

# hakee kenttien tiedot
def hae_kentan_tiedot(icao):

    sql = "SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    kursori = yhteys.cursor()

    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    if tulos:

        return {
            "nimi": tulos[0],
            "matka": (tulos[1], tulos[2])
        }

# kysyy käyttäjältä ensimäisen ja toisen kentän icao koodin
icao1 = input("Anna ensimmäisen kentän ICAO-koodi: ").upper()
icao2 = input("Anna toisen kentän ICAO-koodi: ").upper()

# lisää kentät pää ohjelmaan
kentta1 = hae_kentan_tiedot(icao1)
kentta2= hae_kentan_tiedot(icao2)

# katsoo jos annetuissa koodeissa on kenttö
if kentta1 and kentta2:
    # laskee etäisyyden
    etaisyys = distance.distance(kentta1['matka'], kentta2['matka']).km
    # printaa etäisyyden
    print(f"Antamasi lentokenttien etäisys on {etaisyys:.2f} km.")
else:
    print("Virheelinen koodi")
# kutsuu ohjelman
yhteys.close()
