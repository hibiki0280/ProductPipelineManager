import os
import sqlite3
from six import string_types
from typing import List

from projects import Project


def dict_factory(cursor, row):
   d = {}
   for idx, col in enumerate(cursor.description):
       d[col[0]] = row[idx]
   return d


class ProjectsDB(object):
    def __init__(self, db_path):
        self._conn = sqlite3.connect(os.path.join(db_path, 'projects.db'))
        self._conn.row_factory = dict_factory
        self._cursor = self._conn.cursor()
        self._conn.commit()
        self._table_initialized = False

    def add(self, project):
        if not self._table_initialized:
            self.initialize_table(project)
            self._table_initialized = True

        project.pop("id")
        execute_message = """INSERT INTO 
Projects(%s) VALUES(%s)""" % (", ".join(project.keys()) , ", ".join(["?"]*len(project)))
        
        self._cursor.execute(execute_message, list(project.values())) 
        self._conn.commit()
        
        self._cursor.execute(
            """SELECT id FROM Projects
WHERE name=?""", [project["name"]]
        )
        return self._cursor.fetchone()["id"]

    def initialize_table(self, project):
        columns = ""
        for column in project.keys():
            if column == "id":
                definition = "INTEGER PRIMARY KEY AUTOINCREMENT"
            elif isinstance(column, int):
                definition = "INTEGER"
            elif isinstance(column, string_types):
                definition = "text"

            columns += column + " " + definition +", "
        else:
            columns = '(' + columns.strip(", ") + ')'
            exec_message = "CREATE TABLE IF NOT EXISTS projects %s" % columns

        self._cursor.execute(exec_message)
        

    def get(self, project_id: int) -> Project:
        self._cursor.execute(
            """SELECT * FROM Projects
WHERE id=?""", (str(project_id))
        )
        project = self._cursor.fetchone()
        return project

    def list_projects(self) -> List[Project]:
        self._cursor.execute(
            """SELECT * FROM Projects""")
        projects = self._cursor.fetchall()
        return projects

    def count(self):
        return len(self.list_projects())

    def update(self, project_id, project):
        project.pop("id")
        execute_message = """UPDATE Projects set 
%s where id=?""" % ", ".join(["%s=?" % key for key in project.keys()])
        params = list(project.values())
        params.append(project_id)
        self._cursor.execute(execute_message, params) 
        self._conn.commit()
        

    def delete(self, project_id):
        self._cursor.execute("DELETE FROM Projects where id=?", [project_id])
        self._conn.commit()

    def delete_all(self):
        self._cursor.execute("DELETE FROM Projects")
        self._conn.commit()

    # def unique_id(self):
    #     pass

    def stop_database(self) -> None:
        self._conn.close()
    
def start_database(db_path):
    return ProjectsDB(db_path)


