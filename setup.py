from setuptools import setup

setup(
    name='undercut',
    version='1.0',
    description='An implementation of the undercut game in Python and Flask',
    author='Richard Nai',
    author_email='richardnai6@gmail.com',
    packages=[
        'src.game_logic'
    ],
    include_package_data=True
)