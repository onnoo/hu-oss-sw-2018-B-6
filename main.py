import sqlite3

conn = sqlite3.connect("lab.db")
cur = conn.cursor()

def create_db():
    global conn, cur

    table_create_sql = """create table if not exists todo (
            id integer primary key autoincrement,
            what text not null,
            due text not null,
            finished integer not null);"""

    cur.execute(table_create_sql)

def run_program():
    while True :
        print("Choose what to do:")
        command = input("(a: Add todo, l: List todo, m: Modify todo, c: Check, s: Search, q: Quit)? ")
        print()
        if command == 'a' :
            add_todo()
        elif command == 'l' :
            list_todo()
        elif command == 'm' :
            modify_todo()
        elif command == 'c' :
            check_todo()
        elif command == 's' :
            search_todo()
        elif command == 'q' :
            conn.close()
            break
        else :
            print()

def list_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    sql = "select * from todo where 1"
    cur.execute(sql)

    rows = cur.fetchall()

    for row in rows :
        for i in range(0,len(row)) :
            if i != len(row) - 1 :
                print(row[i], end = " ")
            else :
                print(row[i])

    conn.close()


def add_todo():
    global conn, cur

    todo = input("Todo? ")
    due = input("Due date? ")

    sql = "insert into todo (what, due, finished) values ('" + todo + "', '" + due + "', '0')"
    cur.execute(sql)
    conn.commit()

    print()
    conn.close()

def modify_todo():
    list_todo()

    print()
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    record_id = input("Record_id? ")
    todo = input("Todo? ")
    due = input("Due date? ")
    finished = input("Finished (1: yes, 0: no)? ")

    sql = "UPDATE todo SET what = '"+todo+"', due = '"+due+"', finished = "+finished+" WHERE id = "+record_id
    cur.execute(sql)
    conn.commit()

    print()
    conn.close()

def check_todo():
    global conn, cur

    list_todo()
    print()

    record_id = input("Record_id? ")

    sql = "UPDATE todo SET finished = " + '1' + " WHERE id = " + record_id
    cur.execute(sql)
    conn.commit()
    print("Success Change")

    print()

def search_todo():
    global conn, cur

    search_column = input("(1. ID, 2. What, 3. Due, 4. Finished): ")
    search_column = int(search_column)

    if search_column == 1:
        search_word = input("ID : ")
        search_word = int(search_word)

    elif search_column == 2:
        search_word = input("What : ")

    elif search_column == 3:
        search_word = input("Due : ")

    elif search_column == 4:
        search_word = input("Finished : ")
        search_word = int(search_word)

    sql = "select * from todo where 1"
    cur.execute(sql)

    rows = cur.fetchall()

    no_result_found = 1

    print()
    for row in rows:
        if search_word == row[search_column-1]:
            for i in range(0,len(row)) :
                no_result_found = 0
                if i != len(row) - 1 :
                    print(row[i], end = " ")
                else :
                    print(row[i])
    
    if(no_result_found):
        print("NOT FOUND")
    print()



                    
if __name__ == "__main__":
    create_db()
    run_program()