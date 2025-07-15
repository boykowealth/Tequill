from datetime import datetime

class NotebookSession:
    def __init__(self, session_id=None, title="Untitled", content=""):
        self.session_id = session_id or datetime.now().strftime("%Y%m%d_%H%M%S")
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "session_id": self.session_id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        session = cls(data['session_id'], data['title'], data['content'])
        session.created_at = datetime.fromisoformat(data['created_at'])
        session.updated_at = datetime.fromisoformat(data['updated_at'])
        return session