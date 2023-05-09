import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        port= 5432,
        password="1234")
    
except psycopg2.Error as error:
    print("Errore durante la connessione al database:", error)
    exit()
    
def show_tables():
    cur = conn.cursor()
    print("\nTabella Dept_")
    cur.execute("SELECT * FROM dept")
    rows = cur.fetchall()
    for row in rows:
        print(f"deptno: {row[0]} - dname: {row[1]} - loc: {row[2]}")
        
    cur.execute("SELECT * FROM emp")
    print("\nTabella Emp")
    rows = cur.fetchall()
    for row in rows:
        print(f"empno: {row[0]} - ename : {row[1]} - job: {row[2]} - mgr: {row[3]} - hiredate: {row[4]} - sal: {row[5]} - comm: {row[6]} - deptno: {row[7]}")
        
    cur.execute("SELECT * FROM salgrade")
    print("\nTabella Salgrade")
    rows = cur.fetchall()
    for row in rows:
        print(f"grade: {row[0]} - losal: {row[1]} - hisal: {row[2]}")

def add_dept():
    deptno = input("Inserisci l'id del dipartimento: ")
    dname = input("Inserisci il nome del dipartimento: ")
    loc = input("Inserisci la locazione del dipartimento: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO dept (deptno, dname, loc) VALUES (%s, %s, %s)", (deptno, dname, loc))
    conn.commit()
    print("Dipartimento aggiunto con successo!\n")

def add_emp():
    id = input("Inserisci l'id del dipendente: ")
    ename = input("Inserisci il nome del dipendente: ")
    job = input("Inserisci la posizione del dipendente: ")
    mgr = input("Inserisci l'id del manager: ")
    hiredate = input("Inserisci la data di assunzione (AAAA-MM-GG): ")
    sal = input("Inserisci il salario: ")
    comm = input("Inserisci la commissione: ")
    deptno = input("Inserisci l'id del dipartimento: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO emp (id, ename, job, mgr, hiredate, sal, comm, deptno) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id, ename, job, mgr, hiredate, sal, comm, deptno))
    conn.commit()
    print("Dipendente aggiunto con successo!\n")
    
def add_salgrade():
    grade = input("Inserisci l'id del salario: ")
    losal = input("Inserisci il minimo salario: ")
    hisal = input("Inserisci il massimo salario: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO salgrade (grade, losal, hisal) VALUES (%s, %s, %s)", (grade, losal, hisal))
    conn.commit()
    print("Grado salariale aggiunto con successo.")


def update_dept():
    cur = conn.cursor()

    deptno = input("Inserisci l'id del dipartimento da modificare: ")
    new_dname = input("Inserisci il nuovo nome del dipartimento: ")
    new_loc = input("Inserisci la nuova locazione del dipartimento: ")

    sql = f"UPDATE dept SET dname = '{new_dname}', loc = '{new_loc}' WHERE deptno = {deptno}"
    cur.execute(sql)
    conn.commit()

    print(f"Il dipartimento con id {deptno} è stato modificato con successo")


def delete_dept():
    cur = conn.cursor()

    deptno = input("Inserisci l'id del dipartimento da eliminare: ")

    sql = f"DELETE FROM dept WHERE deptno = {deptno}"
    cur.execute(sql)
    conn.commit()

    print(f"Il dipartimento con id {deptno} è stato eliminato con successo")


def update_emp():
    cur = conn.cursor()

    empno = input("Inserisci l'id del dipendente da modificare: ")
    new_ename = input("Inserisci il nuovo nome del dipendente: ")
    new_job = input("Inserisci il nuovo lavoro del dipendente: ")
    new_mgr = input("Inserisci il nuovo id del manager del dipendente (0 se non ha un manager): ")
    new_hiredate = input("Inserisci la nuova data di assunzione del dipendente (formato YYYY-MM-DD): ")
    new_sal = input("Inserisci il nuovo salario del dipendente: ")
    new_comm = input("Inserisci la nuova commissione del dipendente (0 se non ha una commissione): ")
    new_deptno = input("Inserisci il nuovo id del dipartimento del dipendente: ")

    sql = f"""UPDATE emp 
              SET ename = '{new_ename}', job = '{new_job}', mgr = {new_mgr}, 
                  hiredate = '{new_hiredate}', sal = {new_sal}, comm = {new_comm},
                  deptno = {new_deptno} 
              WHERE empno = {empno}"""
    cur.execute(sql)
    conn.commit()

    print(f"Il dipendente con id {empno} è stato modificato con successo")


def delete_emp():
    cur = conn.cursor()

    empno = input("Inserisci l'id del dipendente da eliminare: ")

    sql = f"DELETE FROM emp WHERE empno = {empno}"
    cur.execute(sql)
    conn.commit()

    print(f"Il dipendente con id {empno} è stato eliminato con successo")
    
def update_salgrade():
    cur = conn.cursor()

    grade = input("Inserisci il grade del salario da modificare: ")
    new_losal = input("Inserisci il nuovo valore del salario minimo: ")
    new_hisal = input("Inserisci il nuovo valore del salario massimo: ")

    cur.execute("UPDATE salgrade SET losal = %s, hisal = %s WHERE grade = %s", (new_losal, new_hisal, grade))
    conn.commit()

    print(f"{cur.rowcount} righe modificate con successo.")

    cur.close()
    
def delete_salgrade():
    cur = conn.cursor()

    grade = input("Inserisci il grade del salario da eliminare: ")
    
    cur.execute("DELETE FROM salgrade WHERE grade = %s", (grade,))
    conn.commit()

    print(f"{cur.rowcount} righe eliminate con successo.")

    cur.close()
    
def search_emp_by_name():
    cur = conn.cursor()

    name = input("\nInserisci il nome dell'impiegato da cercare: ")

    cur.execute("SELECT * FROM emp WHERE ename = %s", (name,))
    result = cur.fetchall()

    if len(result) == 0:
        print("Nessun impiegato trovato con questo nome.")
    else:
        print(f"Trovati {len(result)} impiegati:")
        for row in result:
            print(f"empno: {row[0]} - ename: {row[1]} - job: {row[2]} - mgr: {row[3]} hiredate: - {row[4]} sal: - {row[5]} comm: - {row[6]} - depno: {row[7]}")
    

def menu():
    while True:
        print("\nScegli una delle seguenti opzioni:")
        print("1 - Vedi tutti i record")
        print("2 - Aggiungi un dipartimento")
        print("3 - Aggiungi un dipendente")
        print("4 - Aggiungi un grado salariale")
        print("5 - Aggiorna il dipartimento")
        print("6 - Aggiorna i dipendenti")
        print("7 - Aggiorna il salario")
        print("8 - Elimina il dipartimento")
        print("9 - Elimina il dipendente")
        print("0 - Elimina il salario")
        print("10 - Cerca un dipentente")
        print("11 - Esci da programma")
    
        choice = int(input("Inserisci il numero corrispondente all'opzione scelta: "))
        
        if choice == 1:
            show_tables()
        elif choice == 2:
            add_dept()
        elif choice == 3:
            add_emp()
        elif choice == 4:
            add_salgrade()
        elif choice == 5:
            update_dept()
        elif choice == 6:
            update_emp()
        elif choice == 7:
            update_salgrade()
        elif choice == 8:
            delete_dept()
        elif choice == 9:
            delete_emp()
        elif choice == 0:
            delete_salgrade()
        elif choice == 10:
            search_emp_by_name()
        elif choice == 11:
            print("\nArrivederci!")
            break
        else:
            print("\nScelta non valida. Riprova.")


menu()