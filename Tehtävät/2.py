import mysql.connector

from 1 import yhteys
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='7523',
    autocommit=True
    )

def maa_icao(iso_country):
    sql = F"SELECT type,  count(*) FROM airport WHERE Iso_Country='{iso_country}' group by type"
    kursori= yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()


    if tulos:
        for rivi in tulos:
            print(f" {rivi[0]} , {rivi[1]}")
    else:
        print("tässä maasa ei ole kenttiä")

maa= input("Anna maan koodi esim FI, SE, IE")
maa_icao(maa)
