from pathlib import Path


class ProjectPath:
    projectPath: Path = None
    projectDataDtdPath: Path = None

    @staticmethod
    def get_project_path() -> Path:
        if ProjectPath.projectPath is None:
            ProjectPath.projectPath = Path(__file__).parent.parent.parent.resolve()
        return ProjectPath.projectPath

    @staticmethod
    def get_project_data_dtd_path() -> Path:
        if ProjectPath.projectDataDtdPath is None:
            ProjectPath.projectDataDtdPath = ProjectPath.get_project_path() / 'data' / 'dtd'
        return ProjectPath.projectDataDtdPath
