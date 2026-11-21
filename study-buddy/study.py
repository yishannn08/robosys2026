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
        self.root.geometry("1050x720")
        self.root.minsize(900, 550)
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
        self.currect_page= None

        self.create_main_layout()
        self.show_page("Focus")


    def create_main_layout(self):
header = tk.Frame(
            self.root,
            bg=DARK_BLUE,
            height=65
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="  Study Buddy",
            font=("Arial", 23, "bold"),
            bg=DARK_BLUE,
            fg=WHITE
        ).pack(side="left", padx=18, pady=12)

        tk.Label(
            header,
            text="STUDY • FOCUS • GROW",
            font=("Arial", 10, "bold"),
            bg=DARK_BLUE,
            fg="#C5D5EA"
        ).pack(side="right", padx=25)

        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True)

        # Sidebar
        self.sidebar = tk.Frame(
            body,
            bg="#D5E1F0",
            width=205
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="MENU",
            font=("Arial", 11, "bold"),
            bg="#D5E1F0",
            fg=MUTED
        ).pack(anchor="w", padx=22, pady=(28, 15))

        pages = ["Focus", "Tasks", "Statistics", "Settings"]

        for page in pages:
            tk.Button(
                self.sidebar,
                text=page,
                font=("Arial", 14, "bold"),
                bg="#E8EFF8",
                fg=DARK_BLUE,
                activebackground="#B7CBE3",
                activeforeground=DARK_BLUE,
                relief="flat",
                bd=0,
                cursor="hand2",
                anchor="w",
                padx=18,
                pady=13,
                command=lambda p=page: self.show_page(p)
            ).pack(fill="x", padx=13, pady=7)

        tk.Label(
            self.sidebar,
            text="Keep learning!",
            font=("Arial", 9),
            bg="#D5E1F0",
            fg=MUTED
        ).pack(side="bottom", pady=25)

        self.main_area = tk.Frame(body, bg=BG)
        self.main_area.pack(
            side="left",
            fill="both",
            expand=True,
            padx=18,
            pady=18
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


    def create_focus_page(self):
        self.draw_study_scene(self.page_frame)

        timer_frame = tk.Frame(
            self.page_frame,
            bg=PANEL,
            padx=25,
            pady=20
        )
        timer_frame.pack(fill="x", pady=(0, 18))

        tk.Label(
            timer_frame,
            text="Focus Time",
            font=("Arial", 15, "bold"),
            bg=PANEL,
            fg=DARK_BLUE
        ).pack(pady=(0, 10))

        self.timer_label = tk.Label(
            timer_frame,
            text=self.format_time(self.remaining_seconds),
            font=("Arial", 42, "bold"),
            bg=PANEL,
            fg=BLUE
        )
        self.timer_label.pack(pady=5)

        button_frame = tk.Frame(timer_frame, bg=PANEL)
        button_frame.pack(pady=(12, 0))

        tk.Button(
            button_frame,
            text="Start",
            font=("Arial", 11, "bold"),
            bg=BLUE,
            fg=WHITE,
            activebackground=DARK_BLUE,
            activeforeground=WHITE,
            relief="flat",
            padx=25,
            pady=8,
            command=self.start_timer
        ).pack(side="left", padx=6)

        tk.Button(
            button_frame,
            text="Pause",
            font=("Arial", 11),
            bg=PANEL_BLUE,
            fg=DARK_BLUE,
            relief="flat",
            padx=25,
            pady=8,
            command=self.pause_timer
        ).pack(side="left", padx=6)

        tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 11),
            bg=PANEL_BLUE,
            fg=DARK_BLUE,
            relief="flat",
            padx=25,
            pady=8,
            command=self.reset_timer
        ).pack(side="left", padx=6)

        tk.Label(
            self.page_frame,
            text="Don't forget to take a break.",
            font=("Arial", 11, "italic"),
            bg=BG,
            fg=MUTED
        ).pack(pady=(0, 15))

        task_header = tk.Frame(self.page_frame, bg=BG)
        task_header.pack(fill="x", pady=(5, 10))

        tk.Label(
            task_header,
            text="Today's Tasks",
            font=("Arial", 16, "bold"),
            bg=BG,
            fg=DARK_BLUE
        ).pack(side="left")

        tk.Button(
            task_header,
            text="+ Add",
            font=("Arial", 10, "bold"),
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=15,
            pady=5,
            command=self.add_task
        ).pack(side="right")

        self.today_task_frame = tk.Frame(
            self.page_frame,
            bg=BG
        )
        self.today_task_frame.pack(fill="both", expand=True)

        self.refresh_today_tasks()

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_timer_text(self):
        if self.widget_is_alive(self.timer_label):
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
        if not self.widget_is_alive(self.today_task_frame):
            return

        for widget in self.today_task_frame.winfo_children():
            widget.destroy()

        if not self.tasks:
            tk.Label(
                self.today_task_frame,
                text="No tasks yet. Add a new task!",
                font=("Arial", 11),
                bg=BG,
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
        if not self.widget_is_alive(self.task_list_frame):
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
