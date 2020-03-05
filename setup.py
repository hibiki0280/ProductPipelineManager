"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='projects',
    version='0.1.0',
    license='proprietary',
    description='Project Management',

    author='Hibiki Suzuki',
    author_email='suzukih_pc@yahoo.co.jp',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['six'],
    extras_require={},

    # entry_points={
    #     'console_scripts': [
    #         'tasks = tasks.cli:tasks_cli',
    #     ]
    # },
)