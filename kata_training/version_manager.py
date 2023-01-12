class VersionManager:
    def __init__(self, version):
        self.version = version


t = VersionManager("1.2.3.3")
print(t.version)