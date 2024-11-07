from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("tämä on content", content, "content loppuu")
        data = toml.loads(content)
        # print("tämä on toml:", data)
        
        poetry_data = data.get("tool", {}).get("poetry", {})
        
        name = poetry_data.get("name", "")
        description = poetry_data.get("description", "")
        dependencies = list(poetry_data.get("dependencies", {}).keys())
        dev_dependencies = list(poetry_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys())
        authors = list(poetry_data.get("authors", {}))
        license = poetry_data.get("license", "")


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
