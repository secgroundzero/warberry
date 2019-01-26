import sqlite3
import subprocess

class warberryModel:

    def __init__(self):
        self.conn = sqlite3.connect('warberry.db')
        self.cursor = self.conn.cursor()

    def connectDB(self):
        self.conn = sqlite3.connect('warberry.db')
        self.cursor = self.conn.cursor()

    def insertWarBerryModel(self):
        subprocess.call("sudo cat /proc/cpuinfo | grep Revision | awk {'print $3'} > Results/model", shell=True)
        modelPI="Custom"
        with open('Results/model', 'r') as pi_model:
            for model in pi_model:
                modelPI=model.strip()
        subprocess.call("rm Results/model", shell=True)
        db_in=("WarberryPI", modelPI)
        self.connectDB()
        self.cursor.execute('INSERT INTO warberry (WarBerryName, WarBerryModel) VALUES (?,?)', db_in)
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    
    x=warberryModel()
    x.insertWarBerryModel()


