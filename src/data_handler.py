import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "candidates.json"

def save_candidate_data(candidate_data: dict):
    """Save candidate data to JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Load existing data safely
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                data = json.loads(content) if content else []
        except json.JSONDecodeError:
            data = []
    else:
        data = []

    data.append(candidate_data)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_all_candidates():
    """Load all candidate records."""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                return json.loads(content) if content else []
        except json.JSONDecodeError:
            return []
    return []
