#!/usr/bin/python3
import customtkinter as tk
import random

word_list = ["apple", "banana", "carrot", "dog", "elephant", "frog", "giraffe", "hippo", "iguana", "jaguar", "kiwi", "lemon", "monkey", "newt", "orange", "pear", "quail", "rabbit", "snake", "tiger", "umbrella", "vulture", "walrus", "xylophone", "yak", "zebra", "ant", "bee", "cat", "duck", "eagle", "fish", "goat", "hamster", "insect", "jellyfish", "koala", "lion", "mango", "nut", "octopus", "penguin", "quokka", "raccoon", "seagull", "toucan", "unicorn", "violet", "wombat", "x-ray", "yeti", "zeppelin", "alien", "bear", "caterpillar", "dolphin", "elephant", "flamingo", "gazelle", "hedgehog", "impala", "jellybean", "kangaroo", "llama", "mongoose", "narwhal", "ostrich", "panda", "quokka", "rattlesnake", "sloth", "tiger", "urchin", "vampire", "walrus", "xenomorph", "yak", "zebra", "alligator", "buffalo", "chimpanzee", "dragonfly", "emu", "falcon", "gorilla", "harp", "imp", "jackal", "koala", "lemur", "mantis", "nighthawk", "opossum", "panda"]
adjectives = ["happy", "sad", "big", "small", "bright", "dark", "loud", "quiet", "hot", "cold", "fast", "slow", "angry", "calm", "brave", "fearful", "strong", "weak", "smart", "dumb", "kind", "cruel", "generous", "selfish", "friendly", "hostile", "patient", "impatient", "funny", "serious", "creative", "logical", "honest", "dishonest", "beautiful", "ugly", "tall", "short", "thick", "thin", "rich", "poor", "successful", "unsuccessful", "ambitious", "lazy", "proud", "ashamed", "confident", "doubtful", "clean", "dirty", "healthy", "sick", "fresh", "stale", "delicious", "disgusting", "sweet", "sour", "bitter", "spicy", "fragrant", "stinky", "smooth", "rough", "soft", "hard", "shiny", "dull", "flexible", "rigid", "vibrant", "dull", "colorful", "colorless", "lively", "lifeless", "modern", "ancient", "noisy", "peaceful", "crowded", "empty", "confused", "clear", "solid", "liquid", "gassy", "fragile", "robust", "slippery", "sticky", "sharp", "blunt", "gentle", "harsh", "wet", "dry"]
font_big = ("Arial", 14)
font_medium = ("Arial", 12)

bright_orange = '#F0BF47'
faint_aqua = '#4C8E80'
light_gray = '#B7B7B7'
medium_gray = '#898989'
bright_black = '#3E3E3E'
green = '#74BD71'
console_green = '#8EDA8D'
console_selection = '#5B93C8'

class SbatchGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("sbatch Assistant")

        # Global format
        self.labels_width = 70
        self.sliders_length = 335
        self.job_name_length = 440
        self.main_controls_xmargins = (10,10)
        self.main_controls_ymargins = (5,5)
        self.main_time_font = ("alarm clock", 25)
        self.output_width = 348
        self.command_width = 660
        self.log_width = 500
        self.value_entries_width = 50
        self.time_sliders_height = 90
        self.clock_width = 20

        # Global variables
        self.var_nodes = tk.IntVar()
        self.var_tasks = tk.IntVar()
        self.var_cpus = tk.IntVar()
        self.var_ram = tk.IntVar()

        # Frames
        self.frame_header = tk.CTkFrame(root, fg_color=medium_gray)
        self.frame_name = tk.CTkFrame(self.frame_header, fg_color=medium_gray)
        self.frame_main_controls = tk.CTkFrame(root, fg_color=light_gray)
        self.frame_hours = tk.CTkFrame(self.frame_main_controls, width=500, height=500, fg_color=medium_gray)
        self.frame_nodes = tk.CTkFrame(self.frame_main_controls)
        self.frame_tasks = tk.CTkFrame(self.frame_main_controls)
        self.frame_cpus = tk.CTkFrame(self.frame_main_controls)
        self.frame_ram = tk.CTkFrame(self.frame_main_controls)
        self.frame_log = tk.CTkFrame(self.frame_main_controls)
        self.frame_command = tk.CTkFrame(self.frame_main_controls)
        self.frame_generate = tk.CTkFrame(self.frame_main_controls, fg_color=light_gray)

        self.frame_header.grid(sticky='NWES', row=0, column=0, padx=10, pady=5, columnspan=1)
        self.frame_name.grid(sticky = 'EWS', row=1, column=0, padx=0, pady=(5, 1))
        self.frame_hours.grid(sticky='NWES', row=1, column=1, rowspan=4, columnspan=1, padx=(5,10), pady=10)
        self.frame_main_controls.grid(sticky = 'NWES', row=1, column=0, rowspan=1, columnspan=1, padx=10, pady=10)

        self.frame_nodes.grid(sticky='NWES',row=1, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_tasks.grid(sticky='NWES',row=2, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_cpus.grid(sticky='NWES',row=3, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_ram.grid(sticky='NWES',row=4, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_log.grid(sticky='NWES',row=5, column=0, columnspan=2, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_command.grid(sticky='NWES',row=7, column=0, columnspan=2, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_generate.grid(sticky = 'E', row=8, column=0, columnspan=2, padx=10, pady=self.main_controls_ymargins)

        # Main Time Label
        self.main_time_label = tk.CTkLabel(self.frame_hours, text="0-00:00", text_color=green, fg_color=bright_black, font=self.main_time_font, width=140)
        self.main_time_label.grid(sticky='NWES', row=3, column=1, columnspan=3, padx=5, pady=5)

        # Job Name
        self.job_name_entry = tk.CTkEntry(self.frame_name, width=self.job_name_length, font=font_big, text_color=bright_orange, fg_color = bright_black, corner_radius=1, placeholder_text='Job name')
        self.job_random_name_button = tk.CTkButton(self.frame_name, command=self.get_random_id, text='Random', width=40)
        self.job_name_entry.grid(row=1, column=1, padx=5, pady=10, columnspan=1)
        self.job_random_name_button.grid(sticky = 'E', row=1, column=0, padx=(10,1), pady=10)

        # Number of Nodes
        self.nodes_label = tk.CTkLabel(self.frame_nodes, text="Nodes", width=self.labels_width)
        self.nodes_label.grid(row=0, column=0, padx=10, pady=5)
        self.nodes_entry = tk.CTkSlider(self.frame_nodes, from_=1, to=256, number_of_steps=256, orientation='horizontal', width=self.sliders_length, variable=self.var_nodes)
        self.value_nodes_entry = tk.CTkEntry(self.frame_nodes, textvariable=self.var_nodes, width=self.value_entries_width)
        self.nodes_entry.grid(sticky='E', row=0, column=2, padx=5, pady=5)
        self.value_nodes_entry.grid(row=0, column=3, padx=10, pady=5)
        self.var_nodes.set(1)

        # Number of Tasks
        self.tasks_label = tk.CTkLabel(self.frame_tasks, text="Tasks", width=self.labels_width)
        self.tasks_label.grid(row=0, column=0, padx=10, pady=5)
        self.tasks_entry = tk.CTkSlider(self.frame_tasks, from_=1, to=50, orientation='horizontal', width=self.sliders_length, variable=self.var_tasks)
        self.tasks_entry.grid(sticky='W', row=0, column=1, padx=5, pady=5)
        self.value_tasks_entry = tk.CTkEntry(self.frame_tasks, textvariable=self.var_tasks, width=self.value_entries_width)
        self.value_tasks_entry.grid(row=0, column=3, padx=10, pady=5)
        self.var_tasks.set(1)

        # Number of CPUs per Task
        self.cpus_label = tk.CTkLabel(self.frame_cpus, text="CPUs/Task", width=self.labels_width)
        self.cpus_label.grid(row=0, column=0, padx=10, pady=5)
        self.cpus_entry = tk.CTkSlider(self.frame_cpus, from_=1, to=50, orientation='horizontal', width=self.sliders_length, variable=self.var_cpus)
        self.cpus_entry.grid(row=0, column=1, padx=5, pady=5)
        self.value_cpu_entry = tk.CTkEntry(self.frame_cpus, textvariable=self.var_cpus, width=self.value_entries_width)
        self.value_cpu_entry.grid(row=0, column=3, padx=10, pady=5)
        self.var_cpus.set(1)

        # Memory
        self.memory_label = tk.CTkLabel(self.frame_ram, text="RAM (GB)", width=self.labels_width)
        self.memory_label.grid(sticky='W', row=0, column=0, padx=10, pady=5)
        self.memory_entry = tk.CTkSlider(self.frame_ram, from_=1, to=256, orientation='horizontal', width=self.sliders_length, variable=self.var_ram)
        self.memory_entry.grid(row=0, column=1, padx=5, pady=5)
        self.value_ram_entry = tk.CTkEntry(self.frame_ram, textvariable=self.var_ram, width=self.value_entries_width)
        self.value_ram_entry.grid(row=0, column=3, padx=10, pady=5)
        self.var_ram.set(1)

        # Time
        self.time_days_label = tk.CTkLabel(self.frame_hours, text="Days", fg_color=medium_gray, width=12)
        self.time_hours_label = tk.CTkLabel(self.frame_hours, text="HH", fg_color=medium_gray, width=12)
        self.time_minutes_label = tk.CTkLabel(self.frame_hours, text="MM", fg_color=medium_gray, width=12)
        self.time_days_label.grid(sticky='NEWS', row=0, column=1, padx=5, pady=(5,1))
        self.time_hours_label.grid(sticky='NEWS', row=0, column=2, padx=5, pady=(5,1))
        self.time_minutes_label.grid(sticky='NEWS', row=0, column=3, padx=5, pady=(5,1))
        self.time_days = tk.CTkSlider(self.frame_hours, from_=0, to=7, number_of_steps=7, command=self.refresh_time, orientation='vertical', height=self.time_sliders_height, width=self.clock_width)
        self.time_hours = tk.CTkSlider(self.frame_hours, from_=0, to=23, number_of_steps=23,command=self.refresh_time, orientation='vertical', height=self.time_sliders_height, width=self.clock_width)
        self.time_minutes = tk.CTkSlider(self.frame_hours, from_=0, to=59, number_of_steps=59,command=self.refresh_time, orientation='vertical', height=self.time_sliders_height, width=self.clock_width)
        self.time_days.set(0);  self.time_hours.set(0);  self.time_minutes.set(0)
        self.time_days.grid(sticky='ns', row=2, column=1, padx=5, pady=5)
        self.time_hours.grid(sticky='ns', row=2, column=2, padx=5, pady=5)
        self.time_minutes.grid(sticky='ns', row=2, column=3, padx=5, pady=5)

        # LOG File
        self.log_label = tk.CTkLabel(self.frame_log, text="Log File ", width=self.labels_width)
        self.log_entry = tk.CTkEntry(self.frame_log, width=self.log_width)
        self.log_label.grid(sticky='W', row=0, column=0, padx=5, pady=5)
        self.log_entry.grid(row=0, column=1, padx=10, pady=5)
        self.log_entry.insert(0, 'LOG_%x-%j.txt')

        # Command
        self.command_label = tk.CTkLabel(self.frame_command, text="Command")
        self.command_label.grid(sticky='W', row=0, column=0, padx=10, pady=1)
        self.command_text = tk.CTkTextbox(self.frame_command, height=150, width=self.command_width, wrap=tk.WORD)
        self.command_text.grid(sticky='NESW', row=1, column=0, padx=10, pady=(0,10), columnspan=2)

        # Generate Buttons
        self.generate_command_button = tk.CTkButton(self.frame_generate, text="Generate sbatch Command", command=self.generate_sbatch_command)
        self.generate_report_button = tk.CTkButton(self.frame_generate, text="Generate Report", command=self.generate_report, width=110)
        self.generate_command_button.grid(sticky='E', row=0, column=1, padx=10, pady=10)
        self.generate_report_button.grid(sticky='E', row=0, column=0, padx=0, pady=10)

        # Output
        self.result_label = tk.CTkLabel(root, text="Output")
        self.result_text = tk.CTkTextbox(root, height=150, wrap=tk.WORD, fg_color=bright_black, text_color='white', width=self.output_width)
        self.result_button = tk.CTkButton(root, text='Copy to Clipboard', command=self.copy_result)
        self.result_label.grid(sticky = 'W', row=3, column=0, padx=12, pady=1)
        self.result_text.grid(sticky = 'NEWS', row=4, column=0, padx=10, pady=(0,5))
        self.result_button.grid(sticky='E', row=5, column=0, pady=(5,10), padx=10)
    
    def get_time(self):
        days = str(int(self.time_days.get()))
        hours = str(int(self.time_hours.get())).rjust(2, "0")
        minutes = str(int(self.time_minutes.get())).rjust(2, "0")
        return f'{days}-{hours}:{minutes}:00'
    
    def get_random_id(self):
        self.job_name_entry.delete(0, 'end')
        random_id = f'{random.choice(adjectives)}_{random.choice(word_list)}'
        self.job_name_entry.insert(0, random_id)

    def copy_result(self):
        result = self.result_text.get('1.0', 'end')
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()
        self.result_text.tag_config('highlight', foreground=console_green)
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('1.0', result, 'highlight')

    def generate_sbatch_command(self):
        job_name = self.job_name_entry.get()
        nodes = int(self.nodes_entry.get())
        tasks = int(self.tasks_entry.get())
        cpus = int(self.cpus_entry.get())
        memory = int(self.memory_entry.get())
        time = self.get_time()
        output = self.log_entry.get()
        command = self.command_text.get("1.0", tk.END).strip()

        sbatch_command = f"sbatch --job-name={job_name} --nodes={nodes} --ntasks={tasks} --cpus-per-task={cpus} --mem={memory}G --time={time} --output={output} --wrap=\"{command}\""

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, sbatch_command)

    def generate_report(self):
        job_name = self.job_name_entry.get()
        nodes = int(self.nodes_entry.get())
        tasks = int(self.tasks_entry.get())
        cpus = int(self.cpus_entry.get())
        memory = int(self.memory_entry.get())
        time = self.get_time()
        output = self.log_entry.get()
        command = self.command_text.get("1.0", tk.END).strip()
        report_text = f"""
JOB_NAME\t{job_name}
TIME\t{time}
NODES\t{nodes}
TASKS\t{tasks}
CPUS_PER_TASK\t{cpus}
RAM\t{memory}
OUTPUT\t{output}
COMMAND\t{command}
"""
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, report_text.strip())
    
    def refresh_time(self, _ = None):
        days = int(self.time_days.get())
        hours = str(int(self.time_hours.get())).rjust(2, "0")
        minutes = str(int(self.time_minutes.get())).rjust(2, "0")
        new_time = f'{days}-{hours}:{minutes}'
        self.main_time_label.configure(text = new_time)

if __name__ == "__main__":
    root = tk.CTk()
    root.resizable(False, False)
    app = SbatchGUI(root)
    root.mainloop()
