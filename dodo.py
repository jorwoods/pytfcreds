from pathlib import Path
import shutil

def remove_folder(p: Path) -> bool:
    if not p.exists():
        return True

    shutil.rmtree(p)

    return True

def recursive_remove_files(p: Path, file_glob: str) -> bool:
    for file in p.rglob(file_glob):
        file.unlink()

    return True

def task_clean_build():
    project = Path(__file__).parent
    return {
        "actions": [
            (remove_folder, [project / "build"]),
            (remove_folder, [project / "dist"]),
            (remove_folder, [project / ".eggs"]),
            (recursive_remove_files, [project, "*.egg-info"]),
            (recursive_remove_files, [project, "*.egg"]),
        ]
    }
