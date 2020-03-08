import os
from typing import Any

import entity_database as db
from entity_database import Project, ProjectItem, Asset, Shot


class ProjectFileSystemException(Exception):
    pass


def create_project(project: Project, project_root_path: str):
    if not isinstance(project, Project):
        raise TypeError("project must be Project Object")
    if not isinstance(project_root_path, str):
        raise TypeError("project_root_path must be string")

    if not os.path.isabs(project_root_path):
        project_root_path = os.path.abspath(project_root_path)
    if not os.path.exists(project_root_path):
        raise ProjectFileSystemException("project_root_path does not exists")

    project._set_path(project_root_path)
    id =  db.add(project)
    _create_dir(project, project_root_path)
    return id

    

def _create_dir(entity: Any, parent_dir: str):
    dirname = entity.name.value()
    path = os.path.join(parent_dir, dirname)
    if os.path.exists(path):
        raise ProjectFileSystemException("Project directory: %s already exists" % path)

    os.makedirs(path)

def create_projectitem(projectitem: ProjectItem, project_id: str):
    if not issubclass(type(projectitem), ProjectItem):
        raise TypeError("projectitem must be ProjectItem's subclass")
    if not isinstance(project_id, str):
        raise TypeError("project_id must be string")

    id = db.add_to_project(projectitem, project_id)
    project = db.get(project_id)

    project_root = project.project_root.value()
    project_dir = project.name.value()
    if isinstance(projectitem, Asset):
        base_dir = "Assets"
    elif isinstance(projectitem, Shot):
        base_dir = "Shots"
    else:
        TypeError("projectitem must be Asset or Shot Object")

    parent_dir = os.path.join(project_root, project_dir, base_dir)
    _create_dir(projectitem, parent_dir)
    return id