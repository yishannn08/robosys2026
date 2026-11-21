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


    def create_main_layout(self):
        self.main_frame = tk.Frame(self.root, bg=BG)
        self.main_frame.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(
            self.main_frame,
            bg=DARK_BLUE,
            width=210
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        logo = tk.Label(
            self.sidebar,
            text="Study Buddy",
            font=("Arial", 21, "bold"),
            bg=DARK_BLUE,
            fg=WHITE
        )
        logo.pack(pady=(35, 45))

        self.nav_buttons = {}

        pages = ["Focus", "Tasks", "Statistics", "Settings"]

        for page in pages:
            button = tk.Button(
                self.sidebar,
                text=page,
                font=("Arial", 12),
                bg=DARK_BLUE,
                fg=WHITE,
                activebackground=BLUE,
                activeforeground=WHITE,
                relief="flat",
                bd=0,
                cursor="hand2",
                anchor="w",
                padx=30,
                pady=13,
                command=lambda p=page: self.show_page(p)
            )
            button.pack(fill="x", padx=12, pady=5)
            self.nav_buttons[page] = button

        self.content_frame = tk.Frame(
            self.main_frame,
            bg=BG
        )
        self.content_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        self.header = tk.Frame(
            self.content_frame,
            bg=BG
        )
        self.header.pack(fill="x", padx=35, pady=(25, 10))

        self.page_title = tk.Label(
            self.header,
            text="Focus",
            font=("Arial", 24, "bold"),
            bg=BG,
            fg=DARK_BLUE
        )
        self.page_title.pack(side="left")

        self.page_frame = tk.Frame(
            self.content_frame,
            bg=BG
        )
        self.page_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=15
        )

    def show_page(self, page):
        self.current_page = page

        self.today_task_frame = None
        self.task_list_frame = None
        self.timer_label = None

        for widget in self.page_frame.winfo_children():
            widget.destroy()

        self.page_title.config(text=page)

        for name, button in self.nav_buttons.items():
            if name == page:
                button.config(bg=BLUE)
            else:
                button.config(bg=DARK_BLUE)

        if page == "Focus":
            self.create_focus_page()
        elif page == "Tasks":
            self.create_tasks_page()
        elif page == "Statistics":
            self.create_statistics_page()
        elif page == "Settings":
            self.create_settings_page()
