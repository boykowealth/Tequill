import os
import json
from datetime import datetime

from session import NotebookSession

class NotebookManager:
    def __init__(self, data_dir="notebook_data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def get_all_sessions(self):
        notebooks = []
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".json"):
                path = os.path.join(self.data_dir, fname)
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    notebooks.append(NotebookSession.from_dict(data))
        notebooks.sort(key=lambda x: x.updated_at, reverse=True)
        return notebooks

    def save_session(self, session: NotebookSession):
        session.updated_at = datetime.now()
        path = os.path.join(self.data_dir, f"{session.session_id}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(session.to_dict(), f, ensure_ascii=False, indent=2)

    def delete_session(self, session_id):
        path = os.path.join(self.data_dir, f"{session_id}.json")
        if os.path.exists(path):
            os.remove(path)
