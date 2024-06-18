import csv
import sqlite3
    
def exectue_query(query, params = None, fetchall = True, executemany = False, rows = None):
    try:
        connection = sqlite3.connect(r"C:\\data\\mydb.db")
        cursor = connection.cursor()
        # print(f"Executing query: {query} with params: {params}")
        if not executemany:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
        else:
            cursor.executemany(query, rows)
        if fetchall:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
        # print(f"Query result : {result}")
        connection.commit()
        
        return result
    except Exception as e:
        if connection:
            connection.rollback()
            print("Error occured -", e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
def display_table():
    result = exectue_query('SELECT * FROM DEPT')
    print(result)

def one():
    with open("deptData.csv", "w", newline="") as f:
        wt = csv.writer(f)
        wt.writerow(['ID', 'DEPTNAME','COUNTRY'])
        wt.writerow([10, "Research", "Boston"])
        wt.writerow([20, "Sales", "NewJersey"])
        wt.writerow([30, "HR", "Chennai"])
        wt.writerow([40, "Accounts", "Delhi"])
    print("Data inserted into the csv file!")

def two():
    with open('deptData.csv', 'r') as f:
        rd = csv.reader(f)
        exectue_query('CREATE TABLE IF NOT EXISTS DEPT  (DEPTNO INT, DNAME VARHCAR(20), LOC VARCHR(20));')
        display_table()

def three():
    exectue_query("delete from dept;")

def four():
    #update a row in the table
    deptId = input("Enter deptartment Id : ")
    deptname = input("Enter new name :")
    exectue_query("UPDATE DEPT SET DNAME = '%s' WHERE DEPTNO = %s "%(deptname, deptId))
    display_table()

def five():
    con = ''
    cursor = ""
    try:
        con = sqlite3.connect(r"C:\\data\\tables.sqlite")
        cursor = con.cursor()
        query = 'SELECT * FROM PRODUCT'
        cursor.execute(query)
        get_details = cursor.fetchall()
        print(get_details)
        with open("product.csv", "w", newline="") as f:
            wt = csv.writer(f)
            wt.writerow(['pid', 'pname', 'price'])
            wt.writerows(get_details)
        print("Inserted product table data into product.csv table")
    except sqlite3.DatabaseError as e:
        if con:
            con.rollback()
            print("Error occured - ", e)
    except Exception as e:
        print(f"Error occured - {e}")
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


if __name__ == '__main__':
    print("18-06-2024 - Python Training - Blue Yonder Assignment :")
    print("Assignments On files and sql")
    print("\n1. Create an csv file")
    print("\n2. Read from csv file and store the data in a table using sqlite")
    print("\n3. Delete all data from the table")
    print("\n4. Update contents in a row ")
    print("\n5. Display Table contents")
    print("\n6. Read data from products table and store in csv file")
    print("\n7. Exit")
    n = int(input("\n  Enter a choice: "))
    while n != 7:
        if n==1 : one()
        elif n==2 : two()
        elif n==3 : three()
        elif n==4 : four()
        elif n==5 : display_table()
        elif n==6: five()
        n = int(input("\n  Enter a choice: "))

