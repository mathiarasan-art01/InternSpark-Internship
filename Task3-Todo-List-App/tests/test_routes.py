import os, tempfile, unittest
from app import create_app
from config import Config
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        class T(Config):
            DATABASE_DIR = self.tmp
            DATABASE_PATH = os.path.join(self.tmp, "test.db")
            SCHEMA_PATH = Config.SCHEMA_PATH
            TESTING = True
        self.app = create_app(T)
        self.client = self.app.test_client()
    def test_dashboard_ok(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"TaskNest", r.data)
    def test_add_task_flow(self):
        r = self.client.post("/tasks/add",
            data={"title": "Buy milk", "category": "General",
                  "priority": "Medium", "description": ""},
            follow_redirects=True)
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"Buy milk", r.data)
    def test_404(self):
        r = self.client.get("/no-such-page")
        self.assertEqual(r.status_code, 404)
if __name__ == "__main__":
    unittest.main()
