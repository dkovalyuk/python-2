import sqlite3
from sqlite3 import Error
from contextlib import contextmanager


# https://docs.python.org/3/library/contextlib.html
# https://book.pythontips.com/en/latest/context_managers.html
# https://stackoverflow.com/questions/35489844/what-does-yield-without-value-do-in-context-manager
@contextmanager
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        yield conn
        conn.commit()
    except Error as e:
        conn.rollback()
        print(e)
    finally:
        conn.close()


        
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



sql_create_projects_table = """CREATE TABLE IF NOT EXISTS projects (
 id integer PRIMARY KEY,
 name text NOT NULL,
 begin_date text,
 end_date text
);"""


sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
 id integer PRIMARY KEY,
 name text NOT NULL,
 priority integer,
 project_id integer NOT NULL,
 status_id integer NOT NULL,
 begin_date text NOT NULL,
 end_date text NOT NULL,
 FOREIGN KEY (project_id) REFERENCES projects (id)
);"""


database = './test.db'
with create_connection(database) as conn:
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, project)
    finally:
        cur.close()
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    finally:
        cur.close()
    return cur.lastrowid


with create_connection(database) as conn:
    print(conn)
    # create a new project
    project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
    project_id = create_project(conn, project)
    print(project_id)

    # tasks
    task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
    task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

    # create tasks
    print(create_task(conn, task_1))
    print(create_task(conn, task_2))


def select_projects(conn):
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM projects;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        cur.close()


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


with create_connection(database) as conn:
    print("Projects:")
    select_projects(conn)
    print("\nQuery task by priority:")
    select_task_by_priority(conn,1)

    print("\nQuery all tasks")
    select_all_tasks(conn)



def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, task)
    finally:
        cur.close()


with create_connection(database) as conn:
    update_task(conn, (2, '2015-01-04', '2015-01-06',2))


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    try:
        cur = conn.cursor()
        cur.execute(sql, (id,))
    finally:
        cur.close()


with create_connection(database) as conn:
    delete_task(conn, 1)


sql = """
SELECT tasks.name as tn, projects.name as pn
FROM (tasks join projects on tasks.project_id = projects.id) as joined_table;"""
with create_connection(database) as conn:
    cursor = conn.cursor()
    q_result = cursor.execute(sql)
    for result in q_result.fetchall():
        print(result)                    