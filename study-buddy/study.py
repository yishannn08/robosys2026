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


    def draw_study_scene(self, parent):
        canvas = tk.Canvas(
            parent,
            height=250,
            bg=PANEL_BLUE,
            highlightthickness=0
        )
        canvas.pack(fill="x", pady=(0, 20))

        canvas.create_oval(
            650, -100, 900, 150,
            fill="#C3D2E8",
            outline=""
        )

        canvas.create_rectangle(
            55, 30, 210, 135,
            fill="#F7F9FD",
            outline=BLUE,
            width=3
        )

        canvas.create_line(
            132, 30, 132, 135,
            fill=BLUE,
            width=2
        )

        canvas.create_line(
            55, 82, 210, 82,
            fill=BLUE,
            width=2
        )

        canvas.create_oval(
            75, 45, 105, 75,
            fill="#E6D9A8",
            outline=""
        )

        canvas.create_rectangle(
            0, 185, 850, 250,
            fill="#AABBD2",
            outline=""
        )

        canvas.create_rectangle(
            170, 125, 390, 185,
            fill=DARK_BLUE,
            outline=""
        )

        canvas.create_rectangle(
            180, 135, 380, 175,
            fill="#DCE7F4",
            outline=""
        )

        canvas.create_oval(
            270, 185, 290, 195,
            fill=DARK_BLUE,
            outline=""
        )

        canvas.create_rectangle(
            245, 195, 315, 200,
            fill=DARK_BLUE,
            outline=""
        )

        canvas.create_rectangle(
            440, 155, 545, 165,
            fill="#F7F9FD",
            outline=BLUE
        )

        canvas.create_rectangle(
            450, 145, 540, 155,
            fill="#D8E4F3",
            outline=BLUE
        )

        canvas.create_line(
            600, 185, 600, 105,
            fill=DARK_BLUE,
            width=5
        )

        canvas.create_line(
            600, 110, 650, 85,
            fill=DARK_BLUE,
            width=5
        )

        canvas.create_arc(
            620, 60, 685, 120,
            start=180,
            extent=180,
            fill="#E6D9A8",
            outline=DARK_BLUE,
            width=2
        )

        canvas.create_rectangle(
            690, 165, 710, 185,
            fill="#B8A6A0",
            outline=""
        )

        canvas.create_oval(
            675, 115, 725, 170,
            fill=GREEN,
            outline=""
        )

        canvas.create_oval(
            655, 130, 690, 165,
            fill=GREEN,
            outline=""
        )

        canvas.create_oval(
            705, 125, 740, 165,
            fill=GREEN,
            outline=""
        )

        canvas.create_text(
            110, 155,
            text="Time to study",
            font=("Arial", 12, "bold"),
            fill=DARK_BLUE
        )

        return canvas
