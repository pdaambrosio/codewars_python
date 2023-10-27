from __future__ import annotations

# "It's a class that manages version numbers."
# 
# The class constructor takes a version string as an argument. The version string is in the format
# "major.minor.patch" (e.g. "3.1.7"). If no version string is provided, the default version is "0.0.1"
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


def main() -> None:
    version_manager = VersionManager("1.2.3")
    print(version_manager.release())  # "1.2.3"
    version_manager.major()
    print(version_manager.release())  # "2.0.0"
    version_manager.minor()
    print(version_manager.release())  # "2.1.0"
    version_manager.patch()
    print(version_manager.release())  # "2.1.1"
    version_manager.rollback()
    print(version_manager.release())  # "2.1.0"
    version_manager.rollback()
    print(version_manager.release())  # "2.0.0"
    version_manager.rollback()
    print(version_manager.release())  # "1.2.3"
    

if __name__ == "__main__":
    main()