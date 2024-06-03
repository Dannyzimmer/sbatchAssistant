#!/usr/bin/python3
import tkinter as tk
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
        self.root.title("SLURM sbatch Command Generator")

        # Global format
        self.labels_width = 15
        self.sliders_length = 335
        self.job_name_length = 25
        self.main_controls_xmargins = (10,10)
        self.main_controls_ymargins = (5,5)
        self.main_time_font = ("clean", 14)
        self.output_width = 48
        self.command_width = 55

        # Frames
        self.frame_header = tk.Frame(root, bg=medium_gray)
        self.frame_name = tk.Frame(self.frame_header, bg=medium_gray)
        self.frame_hours = tk.Frame(self.frame_header, width=500, height=500, bg=light_gray)
        self.frame_main_controls = tk.Frame(root, bg=light_gray)
        self.frame_nodes = tk.Frame(self.frame_main_controls)
        self.frame_tasks = tk.Frame(self.frame_main_controls)
        self.frame_cpus = tk.Frame(self.frame_main_controls)
        self.frame_ram = tk.Frame(self.frame_main_controls)
        self.frame_log = tk.Frame(self.frame_main_controls)
        self.frame_temp = tk.Frame(self.frame_main_controls)
        self.frame_command = tk.Frame(self.frame_main_controls)
        self.frame_generate = tk.Frame(self.frame_main_controls, background=light_gray)

        self.frame_header.grid(sticky='NWES', row=0, column=0, padx=10, pady=5, columnspan=1)
        self.frame_name.grid(sticky = 'EWS', row=1, column=0, padx=0, pady=(5, 1))
        self.frame_hours.grid(sticky='NWES', row=0, column=1, rowspan=2, columnspan=1, padx=(10,0), pady=5)
        self.frame_main_controls.grid(sticky = 'NWES', row=1, column=0, rowspan=1, columnspan=1, padx=10, pady=5)

        self.frame_nodes.grid(sticky='NWES',row=1, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_tasks.grid(sticky='NWES',row=2, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_cpus.grid(sticky='NWES',row=3, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_ram.grid(sticky='NWES',row=4, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_log.grid(sticky='NWES',row=5, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_temp.grid(sticky='NWES',row=6, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_command.grid(sticky='NWES',row=7, column=0, padx=self.main_controls_xmargins, pady=self.main_controls_ymargins)
        self.frame_generate.grid(sticky = 'E', row=8, column=0, padx=10, pady=self.main_controls_ymargins)

        # Main Time Label
        self.main_time_label = tk.Label(self.frame_hours, text="0 - 00:00", fg=green, bg=bright_black, font=self.main_time_font)
        self.main_time_label.grid(sticky='NWES', row=3, column=1, columnspan=3, padx=0, pady=0)

        # Job Name
        self.job_name_label = tk.Label(self.frame_name, text="Job Name", bg=medium_gray, font=font_medium)
        self.job_name_entry = tk.Entry(self.frame_name, width=self.job_name_length, font=font_big, fg=bright_orange, bg = bright_black, borderwidth=1)
        self.job_random_name_button = tk.Button(self.frame_name, command=self.get_random_id, text='Random')
        self.job_name_entry.grid(row=1, column=0, padx=10, pady=(0,5), columnspan=2)
        self.job_name_label.grid(sticky='W', row=0, column=0, padx=(10, 8), pady=0)
        self.job_random_name_button.grid(sticky = 'E', row=0, column=1, padx=(0, 5), pady=10)

        # Number of Nodes
        self.nodes_label = tk.Label(self.frame_nodes, text="Number of Nodes", width=self.labels_width)
        self.nodes_label.grid(row=0, column=0, padx=10, pady=5)
        self.nodes_entry = tk.Scale(self.frame_nodes, from_=1, to=256, orient='horizontal', length=self.sliders_length)
        self.nodes_entry.grid(sticky='E', row=0, column=2, padx=5, pady=5)

        # Number of Tasks
        self.tasks_label = tk.Label(self.frame_tasks, text="Number of Tasks", width=self.labels_width)
        self.tasks_label.grid(row=0, column=0, padx=10, pady=5)
        self.tasks_entry = tk.Scale(self.frame_tasks, from_=1, to=50, orient='horizontal', length=self.sliders_length)
        self.tasks_entry.grid(sticky='W', row=0, column=1, padx=5, pady=5)

        # Number of CPUs per Task
        self.cpus_label = tk.Label(self.frame_cpus, text="CPUs per Task", width=self.labels_width)
        self.cpus_label.grid(row=0, column=0, padx=10, pady=5)
        self.cpus_entry = tk.Scale(self.frame_cpus, from_=1, to=50, orient='horizontal', length=self.sliders_length)
        self.cpus_entry.grid(row=0, column=1, padx=5, pady=5)

        # Memory
        self.memory_label = tk.Label(self.frame_ram, text="RAM (GB)", width=self.labels_width)
        self.memory_label.grid(sticky='W', row=0, column=0, padx=10, pady=5)
        self.memory_entry = tk.Scale(self.frame_ram, from_=1, to=256, orient='horizontal', length=self.sliders_length)
        self.memory_entry.grid(row=0, column=1, padx=5, pady=5)

        # Time
        self.time_days_label = tk.Label(self.frame_hours, text="Days", bg=light_gray)
        self.time_hours_label = tk.Label(self.frame_hours, text="HH", bg=light_gray)
        self.time_minutes_label = tk.Label(self.frame_hours, text="MM", bg=light_gray)
        self.time_days_label.grid(row=0, column=1, padx=5, pady=(0,5))
        self.time_hours_label.grid(row=0, column=2, padx=5, pady=(0,5))
        self.time_minutes_label.grid(row=0, column=3, padx=10, pady=(0,5))
        self.time_days = tk.Scale(self.frame_hours, from_=7, to=0, command=self.refresh_time)
        self.time_hours = tk.Scale(self.frame_hours, from_=23, to=0, command=self.refresh_time)
        self.time_minutes = tk.Scale(self.frame_hours, from_=59, to=0, command=self.refresh_time)
        self.time_days.grid(row=2, column=1, padx=5, pady=5)
        self.time_hours.grid(row=2, column=2, padx=5, pady=5)
        self.time_minutes.grid(row=2, column=3, padx=10, pady=5)

        # LOG File
        self.output_label = tk.Label(self.frame_log, text="Log File ", width=self.labels_width)
        self.output_label.grid(sticky='W', row=0, column=0, padx=5, pady=5)
        self.output_entry = tk.Entry(self.frame_log, width=48)
        self.output_entry.grid(row=0, column=1, padx=10, pady=5)
        self.output_entry.insert(0, 'LOG_%x-%j.txt')

        # Command
        self.command_label = tk.Label(self.frame_command, text="Command")
        self.command_label.grid(row=0, column=0, padx=10, pady=5)
        self.command_text = tk.Text(self.frame_command, height=6, width=self.command_width, wrap=tk.WORD)
        self.command_text.grid(sticky='NESW', row=0, column=1, padx=10, pady=5, columnspan=2)

        # Generate Buttons
        self.generate_command_button = tk.Button(self.frame_generate, text="Generate sbatch Command", command=self.generate_sbatch_command)
        self.generate_command_button.grid(row=0, column=0, padx=10, pady=10)
        self.generate_report_button = tk.Button(self.frame_generate, text="Generate Report", command=self.generate_report)
        self.generate_report_button.grid(row=0, column=1, padx=0, pady=10)

        # Output
        self.result_label = tk.Label(root, text="Output")
        self.result_text = tk.Text(root, height=10, wrap=tk.WORD, bg=bright_black, fg='white', 
                                   selectbackground=console_selection, selectforeground='white', width=self.output_width)
        self.result_button = tk.Button(root, text='Copy to Clipboard', command=self.copy_result)
        self.result_label.grid(sticky = 'W', row=3, column=0, padx=10, pady=5)
        self.result_text.grid(sticky = 'NEWS', row=4, column=0, padx=10, pady=5)
        self.result_button.grid(sticky='E', row=5, column=0, pady=5, padx=10)
    
    def get_time(self):
        days = str(self.time_days.get())
        hours = str(self.time_hours.get()).rjust(2, "0")
        minutes = str(self.time_minutes.get()).rjust(2, "0")
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
        nodes = self.nodes_entry.get()
        tasks = self.tasks_entry.get()
        cpus = self.cpus_entry.get()
        memory = self.memory_entry.get()
        time = self.get_time()
        output = self.output_entry.get()
        command = self.command_text.get("1.0", tk.END).strip()

        sbatch_command = f"sbatch --job-name={job_name} --nodes={nodes} --ntasks={tasks} --cpus-per-task={cpus} --mem={memory}GB --time={time} --output={output} --wrap=\"{command}\""

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, sbatch_command)

    def generate_report(self):
        job_name = self.job_name_entry.get()
        nodes = self.nodes_entry.get()
        tasks = self.tasks_entry.get()
        cpus = self.cpus_entry.get()
        memory = self.memory_entry.get()
        time = self.get_time()
        output = self.output_entry.get()
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
        days = self.time_days.get()
        hours = str(self.time_hours.get()).rjust(2, "0")
        minutes = str(self.time_minutes.get()).rjust(2, "0")
        new_time = f'{days} - {hours}:{minutes}'
        self.main_time_label.config(text = new_time)

if __name__ == "__main__":
    root = tk.Tk()
    # root.geometry("445x775")
    root.resizable(False, False)
    app = SbatchGUI(root)
    root.mainloop()
