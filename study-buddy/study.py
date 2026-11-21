import tkinter as tk
from tkinter import messagebox, simpledialog


BG = "#E8EFF8"
PANEL = "#F7F9FD"
PANEL_BLUE = "#D8E4F3"

BLUE = "#7399C9"
DARK_BLUE = "#243B5A"
LAVENDER = "#AEBBD8"

DARK = "#34445D"
MUTED = "#8292A8"
WHITE = "#FFFFFF"
GREEN = "#A8CBBF"


class StudyBuddy:

    def __init__(self, root):
        self.root = root
        self.root.title("Study Buddy")
        self.root.geometry("1100x720")
        self.root.minsize(900, 600)
        self.root.configure(bg=BG)

        self.focus_minutes = 25
        self.remaining_seconds = self.focus_minutes * 60
        self.timer_running = False
        self.timer_job = None

        self.tasks = []
        self.completed_tasks = 0
        self.total_study_minutes = 0

        self.current_page = "Focus"

        self.today_task_frame = None
        self.task_list_frame = None
        self.timer_label = None

        self.create_main_layout()
        self.show_page("Focus")
