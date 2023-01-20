from __future__ import annotations

class VersionManager:
    def __init__(self, version: str = '0.0.1'):
        self.version = version[:5]
        if version == '':
            self.version = '0.0.1'
        assert any(i.isalpha() for i in self.version.replace('.', '')) != True, 'Error occurred while parsing version!'

    def release(self: any) -> str:
        return self.version

    def major(self: any) -> VersionManager:
        self.version = str(int(self.version[0]) + 1) + '.0.0'
        return self

    def minor(self: any) -> VersionManager:
        self.version = self.version[0] + '.' + str(int(self.version[2]) + 1) + '.0'
        return self

    def patch(self: any) -> VersionManager:
        self.version = self.version[0] + '.' + self.version[2] + '.' + str(int(self.version[4]) + 1)
        return self

    def rollback(self: any) -> VersionManager:
        if self.version > 0:
            self.version = self.version[:-1]
        else:
            raise Exception('Cannot rollback!')
        return self


t = VersionManager('1.2.3')
print(t.release())