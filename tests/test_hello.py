import sys
from pathlib import Path

# Ensure the project root is on the Python path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from hello import main  # noqa: E402


def test_main_prints_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Codex!"
