import sqlite3

#database
class Database:
    
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS complaints(
            id Integer Primray Key,
            name text,
            matric text,
            email text,
            address text,
            gender text,
            date text,
            complaint text
        )
        """
        self.cur.execute(sql)
        self.con.commit()
     
    #Insert function
    def insert(self,name,matric,email,address,gender,date,complaint):
        self.cur.execute("insert into complaints values (NULL,?,?,?,?,?,?,?)",
                         (name,matric,email,address,gender,date,complaint))
        self.con.commit()
    
    #Fetch all data from DB
    def fetch(self):
        self.cur.execute("SELECT * from complaints")
        rows=self.cur.fetchall()
        return rows
    
    #Delete a record in DB
    def remove (self,id):
        self.cur.execute("delete from complaints where id=?",(id,))
        self.con.commit()
        
    #Update a record in DB
    def update(self,id,name,matric,email,address,gender,date,complaint):
        self.cur.execute("update complaints set name=?,matric?,email=?,address=?,gender=?,date=?,complaint=? where id=?",
                        (name,matric,email,address,gender,date,complaint,id))
        self.con.commit()
        
       
