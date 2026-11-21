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

    def __init__(self,root):
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
            width=345,
            height=395,
            bg="#6F8FB9",
            highlightthickness=0
        )
        canvas.pack(fill="both", expand=True)

        canvas.create_rectangle(
            0, 0, 345, 395,
            fill="#6F8FB9",
            outline=""
        )

        canvas.create_rectangle(
            20, 25, 185, 205,
            fill="#D8E4F3",
            outline=DARK_BLUE,
            width=3
        )

        canvas.create_oval(
            45, 55, 92, 102,
            fill="#F5E5B5",
            outline=""
        )

        canvas.create_oval(
            62, 45, 108, 91,
            fill="#D8E4F3",
            outline=""
        )

        canvas.create_rectangle(
            99, 25, 105, 205,
            fill="#344F75",
            outline=""
        )

        canvas.create_rectangle(
            20, 112, 185, 118,
            fill="#243B5A",
            outline=""
        )

        canvas.create_text(
            145, 55,
            text="✦",
            fill=WHITE,
            font=("Arial", 15)
        )

        canvas.create_text(
            240, 45,
            text="✦",
            fill=WHITE,
            font=("Arial", 17)
        )

        canvas.create_text(
            205, 100,
            text="✦",
            fill=WHITE,
            font=("Arial", 11)
        )

        canvas.create_rectangle(
            0, 300, 345, 395,
            fill="#344F75",
            outline=""
        )

        canvas.create_rectangle(
            0, 300, 345, 315,
            fill="#243B5A",
            outline=""
        )

        canvas.create_line(
            80, 300, 80, 205,
            fill="#243B5A",
            width=6
        )

        canvas.create_line(
            80, 210, 112, 185,
            fill="#243B5A",
            width=6
        )

        canvas.create_polygon(
            82, 180,
            145, 180,
            125, 210,
            100, 210,
            fill="#F7F9FD",
            outline="#243B5A",
            width=2
        )

        canvas.create_rectangle(
            155, 230, 265, 300,
            fill="#243B5A",
            outline=""
        )

        canvas.create_rectangle(
            163, 237, 257, 290,
            fill="#D8E4F3",
            outline=""
        )

        canvas.create_rectangle(
            198, 290, 220, 300,
            fill="#243B5A",
            outline=""
        )

        canvas.create_oval(
            207, 207, 236, 237,
            fill="#AEBBD8",
            outline=""
        )

        canvas.create_polygon(
            210, 218,
            210, 205,
            221, 213,
            fill="#AEBBD8",
            outline="#8292A8"
        )

        canvas.create_polygon(
            224, 213,
            235, 205,
            234, 220,
            fill="#AEBBD8",
            outline="#8292A8"
        )

        canvas.create_oval(
            214, 218, 217, 221,
            fill="#34445D",
            outline=""
        )

        canvas.create_oval(
            226, 218, 229, 221,
            fill="#34445D",
            outline=""
        )

        canvas.create_polygon(
            219, 223,
            223, 223,
            221, 226,
            fill="#D9BFD0",
            outline=""
        )

        canvas.create_polygon(
            294, 273,
            325, 273,
            320, 300,
            299, 300,
            fill="#C8B3A7",
            outline=""
        )

        canvas.create_line(
            309, 275, 309, 195,
            fill="#426D75",
            width=3
        )

        canvas.create_line(
            309, 238, 291, 218,
            fill="#426D75",
            width=2
        )

        canvas.create_polygon(
            309, 240,
            283, 224,
            292, 218,
            309, 232,
            fill="#789F91",
            outline=""
        )

        canvas.create_polygon(
            309,
 228,
            326, 199,
            329, 211,
            313, 235,
            fill="#789F91",
            outline=""
        )

        canvas.create_polygon(
            309, 211,
            289, 180,
            300, 184,
            311, 205,
            fill="#789F91",
            outline=""
        )

        canvas.create_polygon(
            309, 202,
            315, 175,
            321, 184,
            312, 207,
            fill="#789F91",
            outline=""
        )

        return canvas

    def create_focus_page(self):
        title = tk.Label(
            self.page_frame,
            text="Hey, welcome back!",
            font=("Arial", 25, "bold"),
            bg=BG,
            fg=DARK_BLUE
        )
        title.pack(anchor="w", pady=(0, 15))

        content = tk.Frame(self.page_frame, bg=BG)
        content.pack(fill="both", expand=True)

        left_frame = tk.Frame(
            content,
            bg=BG,
            width=345
        )
        left_frame.pack(side="left", fill="y", padx=(0, 15))
        left_frame.pack_propagate(False)

        scene_frame = tk.Frame(
            left_frame,
            bg=PANEL_BLUE,
            width=345,
            height=395
        )
        scene_frame.pack(fill="x")
        scene_frame.pack_propagate(False)

        self.draw_study_scene(scene_frame)

        tk.Label(
            left_frame,
            text="You can do it!",
            font=("Arial", 14, "bold"),
            bg=BG,
            fg=DARK_BLUE
        ).pack(pady=12)

        right_frame = tk.Frame(content, bg=BG)
        right_frame.pack(side="left", fill="both", expand=True)

        timer_frame = tk.Frame(
            right_frame,
            bg=PANEL,
            padx=15,
            pady=20
        )
        timer_frame.pack(fill="x", pady=(0, 15))

        tk.Label(
            timer_frame,
            text="TIMER",
            font=("Arial", 15, "bold"),
            bg=PANEL,
            fg=DARK_BLUE
        ).pack(pady=(5, 10))

        self.timer_label = tk.Label(
            timer_frame,
            text=self.format_time(self.remaining_seconds),
            font=("Arial", 48, "bold"),
            bg=PANEL,
            fg=DARK_BLUE
        )
        self.timer_label.pack(pady=8)

        button_frame = tk.Frame(timer_frame, bg=PANEL)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Start",
            font=("Arial", 11, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=18,
            pady=9,
            command=self.start_timer
        ).pack(side="left", padx=4)

        tk.Button(
            button_frame,
            text="Pause",
            font=("Arial", 11),
            bg=PANEL_BLUE,
            fg=DARK_BLUE,
            relief="flat",
            padx=18,
            pady=9,
            command=self.pause_timer
        ).pack(side="left", padx=4)

        tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 11),
            bg=PANEL_BLUE,
            fg=DARK_BLUE,
            relief="flat",
            padx=18,
            pady=9,
            command=self.reset_timer
        ).pack(side="left", padx=4)

        task_frame = tk.Frame(
            right_frame,
            bg=PANEL,
            padx=18,
            pady=15
        )
        task_frame.pack(fill="both", expand=True)

        task_header = tk.Frame(task_frame, bg=PANEL)
        task_header.pack(fill="x", pady=(0, 12))

        tk.Label(
            task_header,
            text="Today's Tasks",
            font=("Arial", 16, "bold"),
            bg=PANEL,
            fg=DARK_BLUE
        ).pack(side="left")

        self.today_task_frame = tk.Frame(
            task_frame,
            bg=PANEL
        )
        self.today_task_frame.pack(fill="both", expand=True)

        self.refresh_today_tasks()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer_text(self):
        if self.current_page == "Focus" and self.timer_label:
            self.timer_label.config(
                text=self.format_time(self.remaining_seconds)
        )

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.countdown()

    def countdown(self):
        if not self.timer_running:
            return

        if self.remaining_seconds > 0:
            self.update_timer_text()
            self.remaining_seconds -= 1
            self.timer_job = self.root.after(1000, self.countdown)
        else:
            self.timer_running = False
            self.timer_job = None
            self.total_study_minutes += self.focus_minutes
            self.remaining_seconds = 0
            self.update_timer_text()
            messagebox.showinfo(
                "Study Buddy",
                "Great job! Time to take a break."
            )

    def pause_timer(self):
        self.timer_running = False

        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.update_timer_text()

    def reset_timer(self):
        self.pause_timer()
        self.remaining_seconds = self.focus_minutes * 60
        self.update_timer_text()


    def widget_is_alive(self, widget):
        if widget is None:
            return False

        try:
            return bool(widget.winfo_exists())
        except tk.TclError:
            return False

    def add_task(self):
        task = simpledialog.askstring(
            "New Task",
            "Enter your task:"
        )

        if task and task.strip():
            self.tasks.append({
                "title": task.strip(),
                "done": False
            })

            self.refresh_today_tasks()
            self.refresh_tasks()

    def toggle_task(self, index, variable):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = bool(variable.get())

            self.refresh_today_tasks()
            self.refresh_tasks()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

            self.refresh_today_tasks()
            self.refresh_tasks()

    def refresh_today_tasks(self):
        if self.current_page != "Focus" or not self.today_task_frame:
            return

        for widget in self.today_task_frame.winfo_children():
            widget.destroy()

        if not self.tasks:
            tk.Label(
                self.today_task_frame,
                text="No tasks yet. Add a new task!",
                font=("Arial", 11),
                bg=PANEL,
                fg=MUTED
            ).pack(anchor="w", pady=10)
            return

        for index, task in enumerate(self.tasks):
            row = tk.Frame(
                self.today_task_frame,
                bg=PANEL,
                padx=12,
                pady=8
            )
            row.pack(fill="x", pady=4)

            variable = tk.BooleanVar(value=task["done"])

            tk.Checkbutton(
                row,
                text=task["title"],
                variable=variable,
                command=lambda i=index, v=variable: self.toggle_task(i, v),
                font=("Arial", 11),
                bg=PANEL,
                fg=DARK,
                activebackground=PANEL,
                selectcolor=PANEL_BLUE
            ).pack(side="left", fill="x", expand=True)

            if task["done"]:
                tk.Label(
                    row,
                    text="Done",
                    font=("Arial", 9),
                    bg=PANEL,
                    fg=GREEN
                ).pack(side="right")

    def create_tasks_page(self):
        tk.Label(
            self.page_frame,
            text="Manage your study tasks here.",
            font=("Arial", 11),
            bg=BG,
            fg=MUTED
        ).pack(anchor="w", pady=(0, 15))

        tk.Button(
            self.page_frame,
            text="+ Add Task",
            font=("Arial", 11, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=18,
            pady=8,
            command=self.add_task
        ).pack(anchor="e", pady=(0, 15))

        self.task_list_frame = tk.Frame(
            self.page_frame,
            bg=BG
        )
        self.task_list_frame.pack(fill="both", expand=True)

        self.refresh_tasks()

    def refresh_tasks(self):
        if self.current_page != "Tasks" or not self.task_list_frame:
            return

        for widget in self.task_list_frame.winfo_children():
            widget.destroy()

        if not self.tasks:
            tk.Label(
                self.task_list_frame,
                text="Your task list is empty.",
                font=("Arial", 12),
                bg=BG,
                fg=MUTED
            ).pack(pady=20)
            return

        for index, task in enumerate(self.tasks):
            row = tk.Frame(
                self.task_list_frame,
                bg=PANEL,
                padx=15,
                pady=12
            )
            row.pack(fill="x", pady=5)

            variable = tk.BooleanVar(value=task["done"])

            tk.Checkbutton(
                row,
                text=task["title"],
                variable=variable,
                command=lambda i=index, v=variable: self.toggle_task(i, v),
                font=("Arial", 11),
                bg=PANEL,
                fg=DARK,
                activebackground=PANEL,
                selectcolor=PANEL_BLUE
            ).pack(side="left", fill="x", expand=True)

            tk.Button(
                row,
                text="Delete",
                font=("Arial", 9),
                bg=PANEL_BLUE,
                fg=DARK_BLUE,
                relief="flat",
                padx=12,
                pady=5,
                command=lambda i=index: self.delete_task(i)
            ).pack(side="right")


    def create_statistics_page(self):
        tk.Label(
            self.page_frame,
            text="Keep track of your learning progress.",
            font=("Arial", 11),
            bg=BG,
            fg=MUTED
        ).pack(anchor="w", pady=(0, 25))

        stats_frame = tk.Frame(
            self.page_frame,
            bg=BG
        )
        stats_frame.pack(fill="x")

        completed = sum(
            1 for task in self.tasks if task["done"]
        )

        total = len(self.tasks)

        self.create_stat_card(
            stats_frame,
            "Study Time",
            f"{self.total_study_minutes} min"
        )

        self.create_stat_card(
            stats_frame,
            "Completed Tasks",
            str(completed)
        )

        self.create_stat_card(
            stats_frame,
            "Total Tasks",
            str(total)
        )

        tk.Label(
            self.page_frame,
            text="Small progress is still progress.",
            font=("Arial", 14, "italic"),
            bg=BG,
            fg=BLUE
        ).pack(pady=40)

    def create_stat_card(self, parent, title, value):
        card = tk.Frame(
            parent,
            bg=PANEL,
            padx=25,
            pady=30
        )
        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=8
        )

        tk.Label(
            card,
            text=title,
            font=("Arial", 11),
            bg=PANEL,
            fg=MUTED
        ).pack(pady=(0, 12))

        tk.Label(
            card,
            text=value,
            font=("Arial", 25, "bold"),
            bg=PANEL,
            fg=DARK_BLUE
        ).pack()


    def create_settings_page(self):
        tk.Label(
            self.page_frame,
            text="Customize your study session.",
            font=("Arial", 11),
            bg=BG,
            fg=MUTED
        ).pack(anchor="w", pady=(0, 25))

        settings_frame = tk.Frame(
            self.page_frame,
            bg=PANEL,
            padx=25,
            pady=25
        )
        settings_frame.pack(fill="x")

        tk.Label(
            settings_frame,
            text="Focus Duration",
            font=("Arial", 14, "bold"),
            bg=PANEL,
            fg=DARK_BLUE
        ).pack(anchor="w", pady=(0, 15))

        self.duration_var = tk.IntVar(
            value=self.focus_minutes
        )

        for minutes in [15, 25, 30, 45, 60]:
            tk.Radiobutton(
                settings_frame,
                text=f"{minutes} minutes",
                variable=self.duration_var,
                value=minutes,
                font=("Arial", 11),
                bg=PANEL,
                fg=DARK,
                activebackground=PANEL,
                selectcolor=PANEL_BLUE
            ).pack(anchor="w", pady=5)

        tk.Button(
            settings_frame,
            text="Save Settings",
            font=("Arial", 11, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=8,
            command=self.save_settings
        ).pack(anchor="w", pady=(20, 0))

    def save_settings(self):
        self.pause_timer()

        self.focus_minutes = self.duration_var.get()
        self.remaining_seconds = self.focus_minutes * 60

        messagebox.showinfo(
            "Study Buddy",
            "Settings saved successfully!"
        )

        if self.current_page == "Focus":
            self.update_timer_text()


if __name__ == "__main__":
    root = tk.Tk()
    app = StudyBuddy(root)
    root.mainloop()
