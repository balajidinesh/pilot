import tkinter as tk
import time


def show_toast_with_countdown(message, sleep_time):
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main window

        toast = tk.Toplevel(root)
        toast.overrideredirect(True)  # Removes window decorations
        toast.attributes("-topmost", True)  # Makes the window stay on top

        label = tk.Label(
            toast, padx=10, pady=5,
            bg='#2a914d',
            fg='#FFFFFF',
            font=("Helvetica", 16),
            justify='left',
            highlightthickness=2, highlightbackground="white"
        )

        label.pack()

        # Calculate position for the toast to appear
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_margin = 20  # Margin from the right edge of the screen
        y_margin = 50  # Margin from the top edge of the screen

        # Wrap message if its width exceeds 20% of screen width
        label.config(text=message)
        label_width = label.winfo_reqwidth()
        max_message_width = screen_width * 0.3

        label.config(wraplength=max_message_width)

        rt = sleep_time
        label.config(text=f"{message} ({rt} sec)")
        label.update()
        label_width = label.winfo_reqwidth()

        x = screen_width - label_width - x_margin
        if x < 0:
            x = 0
        y = y_margin

        toast.geometry("+%d+%d" % (x, y))

        remaining_time = sleep_time
        while remaining_time >= 0:
            label.config(text=f"{message} ({remaining_time} sec)")
            remaining_time -= 1
            toast.update()
            time.sleep(1)  # Wait for 1 second

        toast.destroy()
        root.destroy()  # Destroy the main Tk instance

        root.mainloop()  # Start the event loop

    except Exception as e:
        print("Exception at Toast : ", e)
        return False
    return True


# Example usage
# r = show_toast_with_countdown("Waiting for file creation. This is a long message that will be wrapped if necessary...",
#                               sleep_time=5)
# print(r)


t = [
    (2.807692, 5, 0),
    (4.653846, 5.307692, 0),
    (6.807692, 5.461538, 0),
    (6.961538, 6.846154, 0),
    (4.653846, 6.846154, 0),
    (3.115385, 7.0, 0),
    (2.038462, 6.076923, 0)
]

for i in t:
    print(f'make_op("mouse", mouse_mapper(index=0, x={(i[1]/10)-0.2}, y={(i[0]/10)+0.1})),')
