from __future__ import annotations

class VersionManager:
    def __init__(self, version: str = '0.0.1'):
        self.version = version[:5]
        self.prev_version = []
        temporary_version = self.version.split('.')

        if version == '':
            self.version = '0.0.1'

        if len(temporary_version) < 3:
            while len(temporary_version) < 3:
                temporary_version.append('0')
        assert any(i.isalpha() for i in self.version.replace('.', '')) != True, 'Error occurred while parsing version!'

    def release(self: any) -> str:
        return self.version

    def major(self: any) -> VersionManager:
        self.version = str(int(self.version[0]) + 1) + '.0.0'
        return self

    def minor(self: any) -> VersionManager:
        self.prev_version.append(self.version)
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

t = VersionManager('1')
print(t.minor().release())
