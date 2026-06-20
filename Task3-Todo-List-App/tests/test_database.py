import os, tempfile, unittest
from app import create_app
from config import Config
from models import task_model
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        class T(Config):
            DATABASE_DIR = self.tmp
            DATABASE_PATH = os.path.join(self.tmp, "test.db")
            SCHEMA_PATH = Config.SCHEMA_PATH
        self.app = create_app(T)
        self.ctx = self.app.app_context(); self.ctx.push()
    def tearDown(self):
        self.ctx.pop()
    def test_create_and_get_task(self):
        tid = task_model.create_task({"title": "Hello", "priority": "High"})
        row = task_model.get_task(tid)
        self.assertEqual(row["title"], "Hello")
        self.assertEqual(row["priority"], "High")
    def test_toggle_and_delete(self):
        tid = task_model.create_task({"title": "X"})
        task_model.toggle_task(tid)
        self.assertEqual(task_model.get_task(tid)["completed"], 1)
        task_model.delete_task(tid)
        self.assertIsNone(task_model.get_task(tid))
if __name__ == "__main__":
    unittest.main()