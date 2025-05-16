import unittest
from unittest.mock import MagicMock
import tkinter as tk
import random

from buggy_random_gui import RandomNumberApp

class TestRandomNumberApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = RandomNumberApp(self.root)
        self.app.label = MagicMock()
        self.app.root.after = MagicMock(return_value='mock_job_id')

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertFalse(self.app.running)
        self.assertEqual(self.app.button['text'], 'Run')

    def test_toggle_starts_running(self):
        self.app.toggle()
        self.assertTrue(self.app.running)
        self.assertEqual(self.app.button['text'], 'Stop')

    def test_toggle_stops_running(self):
        self.app.running = True
        self.app.toggle()
        self.assertFalse(self.app.running)
        self.assertEqual(self.app.button['text'], 'Run')

    def test_update_numbers_sets_label(self):
        self.app.running = True
        self.app.update_numbers()
        self.app.label.config.assert_called_once()
        args, _ = self.app.label.config.call_args
        number_displayed = args[0]['text']
        self.assertTrue(number_displayed.isdigit())

    def test_update_numbers_does_not_run_when_stopped(self):
        self.app.running = False
        self.app.update_numbers()
        self.app.label.config.assert_not_called()

if __name__ == "__main__":
    unittest.main()
