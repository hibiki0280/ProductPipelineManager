from six import string_types
from typing import List, Any


class Field(object):
    def __init__(self, value: Any):
        self.__value = value

    def value(self):
        return self.__value

    # def set_value(self, value: Any):
    #     self.__value = value

class _Base(object):
    label = "_Base"
    def __init__(self, name=None, description=None, author=None, id=None, *args, **kwagrs):
        if not isinstance(name, string_types):
            raise ValueError('%s.name must be string' % self.__class__.__name__)
        if not ((description is None) or
                isinstance(description, string_types)):
            raise ValueError('%s.description must be string or None' % self.__class__.__name__)
        if not ((author is None) or
                isinstance(author, string_types)):
            raise ValueError('%s.author must be string or None' % self.__class__.__name__)
        
        self.name = Field(name)
        if description:
            self.description = Field(description)
        if author:
            self.author = Field(author)
        self.id = Field(id)

        self._fields = self._asdict().keys()

    def _asdict(self):
        return {field_name: field.value() for field_name, field in self.__dict__.items() if isinstance(field, Field) }

    def _serialize_data(self):
        data = self._asdict()
        data["entitiy_type"] = self.__class__.__name__
        return data

    def __str__(self):
        repr = "%s Object:\r\n" % self.__class__.__name__
        for item in self._asdict().items():
            repr += "    %s: %s\r\n" % item
        return repr

    @staticmethod
    def equivalent(p1, p2) -> bool:
        p1_d = p2._asdict()
        p2_d = p2._asdict()

        for field in p1._fields:
            if field != "id":
                if p1_d[field] != p2_d[field]:
                    return False
                else:
                    continue
        else:
            return True
    @staticmethod
    def is_element(p1,list_projects) -> bool:
        for p2 in list_projects:
            if equivalent(p1,p2):
                return True
        else:
            return False

class Project(_Base):
    label = "Project"
    
class ProjectItem(_Base):
    label = "ProjectItem"
    def __init__(self, *args, **kwargs):        
        super().__init__(*args, **kwargs)
        
        if "project_id" in kwargs:
            self._set_project(kwargs["project_id"])

        
    def _set_project(self, project_id: str) -> None:
        if not isinstance(project_id, str):
            raise ValueError('%s.project_id must be string' % self.__class__.__name__)
        self.project_id = Field(project_id)

class Asset(ProjectItem):
    label = "Asset"

class Shot(ProjectItem):
    label = "Shot"
    


class ProjectException(Exception):
    pass

class AssetException(Exception):
    pass

class ShotException(Exception):
    pass

    
class UninitializedDatabase(Exception):
    pass

def add_to_project(entity, project_id: str) -> str:
    if not issubclass(type(entity), ProjectItem):
        raise TypeError('entity must be Asset or Shot Object')
    if hasattr(entity, "project_id") and entity.project_id is not None:
        raise ValueError('entity.project_id must None')
    if not isinstance(project_id, str):
        raise TypeError('project_id must be string')

    entity._set_project(project_id)
    return add(entity)

def add(entity) -> str:
    if not issubclass(type(entity), _Base):
        raise TypeError('entity must be Project or Asset or Shot Object')
    if hasattr(entity, "project_id") and entity.project_id is None:
        raise ValueError('entity.project_id must not None')
    if entity.id.value() is not None:
        raise ValueError('entity.id must None')

    check_database_status()
    
    project_id = _projectsdb.add(entity._serialize_data())
    return project_id

def get(id: str) -> Project:
    if not isinstance(id, str):
        raise TypeError('project_id must be string')
    check_database_status()
    entity_type, project_dict = _projectsdb.get(id)
    return globals()[entity_type](**project_dict)
        
def list_all():
    check_database_status()
    entities = []
    for entity_type, entity_dict in _projectsdb.list_all():
        entities.append(globals()[entity_type](**entity_dict))
        
    return entities


def count() -> int :
    check_database_status()
    return _projectsdb.count()

def update(id: str, entity: Project) -> None:
    if not isinstance(id, str):
        raise TypeError('project_id must be an int')
    if not issubclass(type(entity), _Base):
        raise TypeError('entity must be ProjectEntity Object or AssetEntity Object')
    check_database_status()

    updates = entity._serialize_data()
    _projectsdb.update(id, updates)

def delete(id: str) -> None:
    if not isinstance(id, str):
        raise TypeError('project_id must be string')
    check_database_status()
    _projectsdb.delete(id)

def delete_all() -> None:
    check_database_status()
    _projectsdb.delete_all()

# def unique_id() -> int:
#     pass

_projectsdb = None

def check_database_status() -> None:
    if _projectsdb is None:
        raise UninitializedDatabase()
    
def start_database(db_path: string_types):
    if not isinstance(db_path, string_types):
        raise TypeError('db_path must be a string')
    global _projectsdb
    from projects import projects_sqlitedb
    _projectsdb = projects_sqlitedb.start_database(db_path)

def stop_database():
    global _projectsdb
    _projectsdb.stop_database()
    _projectsdb = None

