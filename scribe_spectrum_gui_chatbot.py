import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk

class ScribeSpectrumChatbot:
    def __init__(self, master):
        self.master = master
        master.title("Scribe Spectrum Chatbot")
        master.geometry("600x500")
        master.configure(bg="#f0f0f0")

        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=70, height=20, bg="#ffffff")
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.chat_history.config(state=tk.DISABLED)

        self.service_var = tk.StringVar()
        self.service_dropdown = ttk.Combobox(master, textvariable=self.service_var, state="readonly", width=47)
        self.service_dropdown['values'] = ('Select a service', 'Essay Writing', 'Research Papers', 'Thesis Writing', 'Online Classes')
        self.service_dropdown.current(0)
        self.service_dropdown.grid(row=1, column=0, padx=10, pady=10)

        self.select_button = tk.Button(master, text="Get Info", command=self.get_service_info, bg="#4CAF50", fg="white")
        self.select_button.grid(row=1, column=1, padx=10, pady=10)

        self.user_input = tk.Entry(master, width=50, bg="#ffffff")
        self.user_input.grid(row=2, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Send", command=self.send_message, bg="#008CBA", fg="white")
        self.send_button.grid(row=2, column=1, padx=10, pady=10)

        self.display_message("Chatbot: Welcome to Scribe Spectrum Agency! Please select a service from the dropdown menu to learn more about our offerings.")

    def display_message(self, message):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, message + "\n\n")
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.see(tk.END)

    def get_service_info(self):
        selected_service = self.service_var.get()
        if selected_service == "Select a service":
            self.display_message("Chatbot: Please select a specific service to get more information.")
        else:
            info = self.get_service_details(selected_service)
            self.display_message(f"Chatbot: Here's information about our {selected_service} service:\n\n{info}")

    def get_service_details(self, service):
        services = {
            "Essay Writing": """Our Essay Writing service includes:
• Custom-written essays tailored to your requirements
• In-depth research and proper citations
• Plagiarism-free content
• Timely delivery
• Various academic levels and subjects covered

Do you have any specific questions about our Essay Writing service?""",

            "Research Papers": """Our Research Papers service offers:
• Comprehensive literature reviews
• Data analysis and interpretation
• Proper formatting and citation styles (APA, MLA, Chicago, etc.)
• Expert writers in various fields
• Regular progress updates

Is there a particular aspect of research paper writing you need help with?""",

            "Thesis Writing": """Our Thesis Writing service provides:
• Assistance in developing your thesis statement
• Structured approach to dissertation writing
• In-depth research and analysis
• Editing and proofreading
• Regular consultations with expert writers

What stage of the thesis writing process are you currently in?""",

            "Online Classes": """Our Online Classes assistance includes:
• Regular participation in online discussions
• Completion of assignments and quizzes
• Exam preparation
• One-on-one tutoring sessions
• Course material comprehension support

Which aspects of your online class do you need help with?"""
        }
        return services.get(service, "Information about this service is not available.")

    def send_message(self, event=None):
        user_message = self.user_input.get()
        if user_message.strip() != "":
            self.display_message("You: " + user_message)
            self.user_input.delete(0, tk.END)
            
            response = self.get_response(user_message)
            self.display_message("Chatbot: " + response)

        if user_message.lower() in ["quit", "exit", "bye"]:
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.master.quit()

    def get_response(self, message):
        message = message.lower()
        if "price" in message or "cost" in message:
            return "Our pricing varies depending on the type of service, academic level, and deadline. For a personalized quote, please provide more details about your project or visit our website."
        elif "deadline" in message or "turnaround" in message:
            return "We offer flexible turnaround times to meet your needs. Depending on the complexity of the project, we can deliver work within 24 hours to several weeks. What's your required deadline?"
        elif "quality" in message or "plagiarism" in message:
            return "We take quality very seriously. All our work is original, plagiarism-free, and goes through a rigorous quality check process. We also offer free revisions to ensure your complete satisfaction."
        elif "writer" in message or "expert" in message:
            return "Our team consists of experienced writers and subject matter experts with advanced degrees in various fields. We match your project with the most suitable expert to ensure high-quality results."
        else:
            return "Thank you for your question. To best assist you, please select a specific service from the dropdown menu above, and I'll provide you with detailed information about that service."

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = ScribeSpectrumChatbot(root)
    root.mainloop()