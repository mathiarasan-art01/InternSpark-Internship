import os, tempfile, unittest, json
from app import create_app
from config import Config
class TestApi(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        class T(Config):
            DATABASE_DIR = self.tmp
            DATABASE_PATH = os.path.join(self.tmp, "test.db")
            SCHEMA_PATH = Config.SCHEMA_PATH
            TESTING = True
        self.app = create_app(T)
        self.client = self.app.test_client()
    def test_create_and_list(self):
        r = self.client.post("/api/tasks", json={"title": "API task", "priority": "High"})
        self.assertEqual(r.status_code, 201)
        tid = r.get_json()["id"]
        r2 = self.client.get("/api/tasks")
        self.assertEqual(r2.status_code, 200)
        titles = [t["title"] for t in r2.get_json()]
        self.assertIn("API task", titles)
        r3 = self.client.get(f"/api/tasks/{tid}")
        self.assertEqual(r3.get_json()["priority"], "High")
    def test_stats(self):
        r = self.client.get("/api/stats")
        self.assertEqual(r.status_code, 200)
        self.assertIn("total", r.get_json())
if __name__ == "__main__":
    unittest.main()
