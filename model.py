import sqlite3
import baza

conn = sqlite3.connect("baza.sqlite3")

# TODO: Tukaj moramo ustvarit bazo če je še ni

baza.pripravi_vse(conn)

class Model:
    def dobi_vse_uporabnike(self):
        with conn:
            cur = conn.execute("""
            SELECT * FROM uporabnik
            """)

            return cur.fetchall()
    
    



