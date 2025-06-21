import tkinter as tk
from tkinter import ttk, messagebox

class EnergyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Unit Converter")
        self.root.geometry("400x500")
        self.root.resizable(True, True)

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')

        self.setup_ui()

    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="Energy Unit Converter", 
                              font=("Arial", 16, "bold"), fg="darkblue")
        title_label.pack(pady=20)

        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Convert From", padding="10")
        input_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Label(input_frame, text="Value:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.input_var = tk.StringVar()
        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_var, width=15)
        self.input_entry.grid(row=0, column=1, padx=(10, 0), pady=5)

        tk.Label(input_frame, text="Unit:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.from_unit = tk.StringVar(value="Joules")
        from_combo = ttk.Combobox(input_frame, textvariable=self.from_unit, 
                                 values=["Joules", "Calories", "Kilowatt-hours"], 
                                 state="readonly", width=12)
        from_combo.grid(row=1, column=1, padx=(10, 0), pady=5)

        # Output section
        output_frame = ttk.LabelFrame(main_frame, text="Convert To", padding="10")
        output_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Label(output_frame, text="Unit:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.to_unit = tk.StringVar(value="Calories")
        to_combo = ttk.Combobox(output_frame, textvariable=self.to_unit, 
                               values=["Joules", "Calories", "Kilowatt-hours"], 
                               state="readonly", width=12)
        to_combo.grid(row=0, column=1, padx=(10, 0), pady=5)

        tk.Label(output_frame, text="Result:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.result_var = tk.StringVar(value="0")
        result_entry = ttk.Entry(output_frame, textvariable=self.result_var, 
                               state="readonly", width=15)
        result_entry.grid(row=1, column=1, padx=(10, 0), pady=5)

        # Convert button
        convert_btn = ttk.Button(main_frame, text="Convert", command=self.convert_energy)
        convert_btn.pack(pady=10)

        # Clear button
        clear_btn = ttk.Button(main_frame, text="Clear", command=self.clear_fields)
        clear_btn.pack(pady=5)

        # Bind Enter key to convert
        self.root.bind('<Return>', lambda e: self.convert_energy())

    def convert_energy(self):
        try:
            input_value = float(self.input_var.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            # Convert to joules first (base unit)
            joules = self.to_joules(input_value, from_unit)

            # Convert from joules to target unit
            result = self.from_joules(joules, to_unit)

            # Format result (show up to 6 decimal places, remove trailing zeros)
            self.result_var.set(f"{result:.6f}".rstrip('0').rstrip('.'))

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion error: {str(e)}")

    def to_joules(self, value, unit):
        """Convert any unit to joules"""
        conversions = {
            "Joules": 1,
            "Calories": 4.184,  # 1 calorie = 4.184 joules
            "Kilowatt-hours": 3600000  # 1 kWh = 3.6 × 10^6 joules
        }
        return value * conversions[unit]

    def from_joules(self, joules, unit):
        """Convert joules to any unit"""
        conversions = {
            "Joules": 1,
            "Calories": 1/4.184,
            "Kilowatt-hours": 1/3600000
        }
        return joules * conversions[unit]

    def clear_fields(self):
        self.input_var.set("")
        self.result_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyConverter(root)
    root.mainloop()
