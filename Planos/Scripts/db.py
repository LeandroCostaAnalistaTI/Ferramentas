import psycopg2

class DB:
   db = None
   
   def __init__(self, host, database, user, password):
    self.db = psycopg2.connect(host=ec2-3-225-30-189.compute-1.amazonaws.com, database=d3503a8lv953eh, user=jyyfsvutdccsds,  password=dbff6778cdd9c5e787c459110680caf74ce277d84ece6c27590202b44f17d988)

    def insert(self, sql):
        try:
            cur = self.db.cursor()
            cur.execute(sql)
            cur.close()

            self.db.commit()
        except:
            return False
        return True

    def select(self, sql):
        result = None
        try:
            cur = self.db.cursor()
            cur.execute(sql)
            result = cur.fetchall()
        except:
            return None
        return result
        
    def close(self):
        self.db.close()
