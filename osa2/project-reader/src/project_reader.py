from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        parsed_toml = toml.loads(content)

        poertyreitti = parsed_toml.get("tool").get("poetry")
        name = poertyreitti.get("name")
        des = poertyreitti.get("description")
        lisenssi = poertyreitti.get("license")
        dep = poertyreitti.get("dependencies")
        devdep = poertyreitti.get("group").get("dev").get("dependencies")
        authors = poertyreitti.get("authors")





        print(parsed_toml)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, des, dep, devdep, lisenssi, authors)
