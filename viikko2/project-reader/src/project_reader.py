from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        content_string = toml.loads(content)

        name=content_string["tool"]["poetry"]["name"]

        description=content_string["tool"]["poetry"]["description"]

        dependencies=[]
        for i in content_string["tool"]["poetry"]["dependencies"]:
            dependencies.append(i)
        
        dev_dependencies=[]
        for i in content_string["tool"]["poetry"]["group"]["dev"]["dependencies"]:
            dev_dependencies.append(i)
        
        license=content_string["tool"]["poetry"]["license"]

        authors=[]
        for i in content_string["tool"]["poetry"]["authors"]:
            authors.append(i)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
