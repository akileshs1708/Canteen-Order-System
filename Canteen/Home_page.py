import tkinter as tk
root = tk.Tk()
root.geometry("1000x700")
root.title("Canteen Food Ordering System")


def open_admin_mode():
    root.destroy()

def open_staff_student_mode():
    buttonFrame.destroy()
    id_input_frame = tk.Frame(root)
    id_input_frame.pack(pady=20)


    def submit_id():
        id_number = id_entry.get()
        print("Entered ID Number:", id_number)
        root.destroy()
        from .update import allFrames_menu
        allFrames_menu()

    id_label = tk.Label(id_input_frame, text="Enter ID Number:")
    id_label.pack(pady=10)
    id_entry = tk.Entry(id_input_frame)
    id_entry.pack(pady=5)

    submit_button = tk.Button(id_input_frame, text="Submit", command=submit_id)
    submit_button.pack(pady=10)

def create_home_page_widgets():
    title_label = tk.Label(root, text="Welcome to Canteen Food Ordering System", font=("bold", 18))
    title_label.pack(pady=20)

    global buttonFrame
    buttonFrame = tk.Frame(root)
    buttonFrame.pack(pady=10)

    admin_button = tk.Button(buttonFrame, text="Admin Mode", command=open_admin_mode, width=20, height=2)
    admin_button.pack(side=tk.LEFT, padx=10)

    staff_student_button = tk.Button(buttonFrame, text="Staff/Student Mode", command=open_staff_student_mode, width=20, height=2)
    staff_student_button.pack(side=tk.RIGHT, padx=10)

create_home_page_widgets()
root.mainloop()