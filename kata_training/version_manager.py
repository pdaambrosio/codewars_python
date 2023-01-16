class VersionManager:
    def __init__(self, version: str = '0.0.1'):
        self.version = version[:5]
        assert any(i.isalpha() for i in self.version.replace('.', '')) != True, 'Invalid version format'


t = VersionManager('1.a.3.4')
print(t.version)


test = '1.a.3.4'
print([i.isalpha() for i in test.replace('.', '')])
