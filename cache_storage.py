from pathlib import Path
current_dir = Path.cwd()

class CacheStorage():
    def __init__(self, target_dir:str):
        self.target_dir = target_dir
        self.objects_dir = current_dir / self.target_dir / 'objects'
        self.metadata_dir = current_dir / self.target_dir / 'metadata'

        self.main_dir = current_dir / self.target_dir
        self.objects_dir.mkdir(parents=True, exist_ok=True)
        self.metadata_dir.mkdir(parents=True, exist_ok=True)

    # implemet:
    # recieve url
    # hash it
    # save it to objects
    # create an object and save it too
cache = CacheStorage('cache')
print(cache.main_dir)