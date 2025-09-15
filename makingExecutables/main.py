import pandas as pd
from tkinter import Tk, filedialog
import os

# hide main window
Tk().withdraw()


# ask user to choose the filename with path
file_path = filedialog.askopenfilename(title="Select the Excel file", filetypes=[("Excel files", "*.xlsx *.xls")])

# load file make description and show result
df = pd.read_excel(file_path)
description = df.describe()
description.to_csv("report.csv")

print(f"Report saved as {os.path.abspath('report.csv')}")
