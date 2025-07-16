from pathlib import Path
import json
from datetime import datetime
from session import NotebookSession

class NotebookManager:
    def __init__(self):
        self.default_data_dir = Path("notebook_data")

        self.user_data_dir = Path.home() / ".tequill"
        self.user_data_dir.mkdir(parents=True, exist_ok=True)

    def get_all_sessions(self):
        sessions = {}

        for path in self.user_data_dir.glob("*.json"):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    session = NotebookSession.from_dict(json.load(f))
                    sessions[session.session_id] = session
            except Exception as e:
                print(f"Failed to load user notebook {path.name}: {e}")

        if self.default_data_dir.exists():
            for path in self.default_data_dir.glob("*.json"):
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        session = NotebookSession.from_dict(json.load(f))
                        if session.session_id not in sessions:
                            sessions[session.session_id] = session
                except Exception as e:
                    print(f"Failed to load default notebook {path.name}: {e}")

        return sorted(sessions.values(), key=lambda x: x.updated_at, reverse=True)

    def save_session(self, session: NotebookSession):
        session.updated_at = datetime.now()
        path = self.user_data_dir / f"{session.session_id}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(session.to_dict(), f, ensure_ascii=False, indent=2)

    def delete_session(self, session_id):
        path = self.user_data_dir / f"{session_id}.json"
        if path.exists():
            path.unlink()
