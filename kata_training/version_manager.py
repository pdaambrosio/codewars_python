from __future__ import annotations

class VersionManager:
    def __init__(self, version: str = '0.0.1') -> None:
        self.previous_version = []
        self.version = version
        test_version: list[str] = ((version or "0.0.1") + ".0.0").split('.')[:3]
        assert all(i.isdigit() for i in test_version), "Error occured while parsing version!"
        self.major_version, self.minor_version, self.patch_version = map(int, test_version)

    def release(self) -> str:
        return f"{self.major_version}.{self.minor_version}.{self.patch_version}"

    def major(self) -> VersionManager:
        self.previous_version.append((self.major_version, self.minor_version, self.patch_version))
        self.major_version, self.minor_version, self.patch_version = self.major_version + 1, 0, 0
        return self

    def minor(self) -> VersionManager:
        self.previous_version.append((self.major_version, self.minor_version, self.patch_version))
        self.minor_version, self.patch_version = self.minor_version + 1, 0
        return self

    def patch(self) -> VersionManager:
        self.previous_version.append((self.major_version, self.minor_version, self.patch_version))
        self.patch_version += 1
        return self

    def rollback(self) -> VersionManager:
        assert self.previous_version, "Cannot rollback!"
        self.major_version, self.minor_version, self.patch_version = self.previous_version.pop()
        return self


t1 = VersionManager('1.2.3')
print(t1.major().minor().patch().release())

t2 = VersionManager('a.b.c')
print(t2.major().rollback().release())
