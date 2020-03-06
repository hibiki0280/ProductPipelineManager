from six import string_types
from typing import List, Any


class Field(object):
    def __init__(self, value: Any):
        self.__value = value

    def value(self):
        return self.__value


class _BaseEntity(object):
    label = "entity"
    def __init__(self, name=None, description=None, author=None, id=None):
        if not isinstance(name, string_types):
            raise ValueError('%s.name must be string' % self.label)
        if not ((description is None) or
                isinstance(description, string_types)):
            raise ValueError('%s.description must be string or None' % self.label)
        if not ((author is None) or
                isinstance(author, string_types)):
            raise ValueError('%s.author must be string or None' % self.label)
        
        self.name = Field(name)
        if description:
            self.description = Field(description)
        if author:
            self.author = Field(author)
        self.id = Field(id)

        self._fields = self._asdict().keys()

    def _asdict(self):
        return {field_name: field.value() for field_name, field in self.__dict__.items() if isinstance(field, Field) }

    def __str__(self):
        repr = "%s Object:\r\n" % self.label
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

class ProjectEntity(_BaseEntity):
    label = "ProjectEntitiy"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class AssetEntity(_BaseEntity):
    label = "AssetEntity"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.project_id = None
        
    def _set_project(self, project_id: int) -> None:
        # if not isinstance(project_id, int):
        #     raise ValueError('%s.project_id must be int' % self.label)
        self.project_id = Field(project_id)


class ProjectEntityException(Exception):
    pass

class AssetEntityException(Exception):
    pass

    
class UninitializedDatabase(Exception):
    pass

def add_to_project(entity, project_id: int) -> int:
    if not isinstance(entity, AssetEntity):
        raise TypeError('entity must be AssetEntity Object')
    if hasattr(entity, "project_id") and entity.project_id is not None:
        raise ValueError('entity.project_id must None')
    if not isinstance(project_id, int):
        raise TypeError('project_id must be an int')

    entity._set_project(project_id)
    return add(entity)

def add(entity) -> int:
    if not issubclass(type(entity), _BaseEntity):
        raise TypeError('entity must be ProjectEntity Object or AssetEntity Object')
    if entity.id.value() is not None:
        raise ValueError('entity.id must None')

    

    check_database_status()
    
    project_id = _projectsdb.add(entity._asdict())
    return project_id

def get(project_id: int) -> ProjectEntity:
    if not isinstance(project_id, int):
        raise TypeError('project_id must be an int')
    check_database_status()
    project_dict = _projectsdb.get(project_id)
    return ProjectEntity(**project_dict)

def list_projects() -> List[ProjectEntity]:
    check_database_status()
    return [ProjectEntity(**prj) for prj in _projectsdb.list_projects()]

def count() -> int :
    check_database_status()
    return _projectsdb.count()

def update(project_id: int, project: ProjectEntity) -> None:
    if not isinstance(project_id, int):
        raise TypeError('project_id must be an int')
    if not isinstance(project, ProjectEntity):
        raise TypeError('project must be an Project Object')
    check_database_status()

    updates = project._asdict()
    _projectsdb.update(project_id, updates)

def delete(project_id: int) -> None:
    if not isinstance(project_id, int):
        raise TypeError('project_id must be an int')
    check_database_status()
    _projectsdb.delete(project_id)

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

