import os
import sqlite3
import uuid
from uuid import UUID
from six import string_types
from typing import List

from entity_database import Project


def dict_factory(cursor, row):
   d = {}
   for idx, col in enumerate(cursor.description):
       d[col[0]] = row[idx]
   return d


class EntitiesDB(object):
    def __init__(self, db_path):
        self._conn = sqlite3.connect(os.path.join(db_path, 'entity_database.db'))
        self._conn.row_factory = dict_factory
        self._cursor = self._conn.cursor()
        self._conn.commit()

        self._tables = {}
        
    def add(self, entity):
        self.initialize_entity_table_if_not(entity)

        entity["id"] = self.unique_id()
        execute_message = """INSERT INTO 
%s(%s) VALUES(%s)""" % (self.tablename(entity),", ".join(entity.keys()) , ", ".join(["?"]*len(entity)))
        
        self._cursor.execute(execute_message, list(entity.values())) 
        self._conn.commit()
        
        return entity["id"]

    def list_tables(self):
        self._cursor.execute("select name from sqlite_master where type='table'")
        return [table["name"] for table in self._cursor.fetchall()]

    def tablename(self, entity) -> str:
        return entity["entitiy_type"]
        
    def initialize_entity_table_if_not(self, entity):
        if not self._tables.get(self.tablename(entity)):
            self._initialize_table(entity)
            return False
        else:
            return True

    def _initialize_table(self, entity):
        columns = ""
        for column in entity.keys():
            if column == "id":
                definition = "text"
            elif isinstance(column, int):
                definition = "INTEGER"
            elif isinstance(column, string_types):
                definition = "text"

            columns += column + " " + definition +", "
        else:
            columns = '(' + columns.strip(", ") + ')'
            exec_message = """CREATE TABLE IF NOT EXISTS 
{tablename} {columns}""".format(tablename=self.tablename(entity), columns=columns)
            

        self._cursor.execute(exec_message)
        self._tables[self.tablename(entity)] =True
        

    def get(self, entity_id: str):
        for table in self.list_tables():
            self._cursor.execute(
                """SELECT * FROM %s
WHERE id=?""" % table, (entity_id,)
            )
            entity = self._cursor.fetchone()
            if not entity:
                continue
            else:
                return table, entity
        else:
            return None
    
    def list_items(self, project_id: str, entity_type: str):
        self._cursor.execute(
            """SELECT * FROM %s WHERE project_id=?""" % entity_type, (project_id,))
        return self._cursor.fetchall()
        
    def list_all(self) -> List[Project]:
        entities = []
        for table in self.list_tables():
            self._cursor.execute(
                """SELECT * FROM %s""" % table)
            entities += [ (table, entity) for entity in self._cursor.fetchall()]
        return entities

    def count(self):
        return len(self.list_all())

    def update(self, project_id, entity):
        entity.pop("id")
        execute_message = """UPDATE %s set 
%s where id=?""" % (self.tablename(entity), ", ".join(["%s=?" % key for key in entity.keys()]))
        params = list(entity.values())
        params.append(project_id)
        self._cursor.execute(execute_message, params) 
        self._conn.commit()
        

    def delete(self, project_id):
        for table in self.list_tables():
            self._cursor.execute("DELETE FROM %s where id=?" % table, [project_id])
        self._conn.commit()

    def delete_all(self):
        for table in self.list_tables():
            self._cursor.execute("DELETE FROM %s" % table)
        self._conn.commit()

    def unique_id(self) -> str:
        return str(uuid.uuid4())

    def stop_database(self) -> None:
        self._conn.close()
    
def start_database(db_path):
    return EntitiesDB(db_path)


