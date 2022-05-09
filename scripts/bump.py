from datetime import datetime
from pathlib import Path

from cleaner_data import __version__

print("Bumping version")
today = datetime.utcnow().date().strftime("%Y%m%d")

major, version_date = __version__.split(".")

if version_date.startswith(today):
    v = int(version_date[-2:]) + 1
else:
    v = 0


new_version = f"{major}.{today}{v:>02}"

print("New version", new_version)


about = Path(__file__).parents[1] / "cleaner_data" / "__about__.py"
about.write_text(f'__version__ = "{new_version}"\n')  # cant use !r because it uses '
