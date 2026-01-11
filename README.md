# Financial Circle

A simple desktop application built with Tkinter that lets you input variables with associated percentages, visualize them as a pie chart, and manage the data in a live table.

## Features                     
- Add variables with a corresponding percentage (0-100)               
- Automatically builds a pie chart from entered data
- If total percentage is less than 100%, it automatically adds a "Other" slice         
- Live table display of variables and their percentages           
- Clear all inputs and data                         
- Basic input validation with user-friendly messages               
- Pretty table rendering for a clean console/table view (within the UI)                    

## Prerequisites
- Python 3.8+
- pip

## Installation
1.Clone or download the repository.
2.Install required Python packages:

- Tkinter (usually comes with Python standard library)
- matplotlib
- prettytable

Example (ensure you have a working Python environment):
```

pip install matplotlib prettytable

```
> Note: Tkinter is typically included with Python on most platforms. If you encounter issues, install the appropriate Tkinter package for your OS.

Note: Tkinter is typically included with Python on most platforms. If you encounter issues, install the appropriate Tkinter package for your OS.

## Usage
1.Run the script:
```

python main.py

```
2.In the application window:
- Enter a variable name in "Переменная" and its percentage in "Процент".
- Click "Добавить" to append to the list and update the table.
- Click "Построить круг" to render a pie chart of all variables. If the total is less than 100%, a slice named "Другие" (Other) will be - added to complete the circle.
- Click "очистить переменные" to clear all data.
- The table at the bottom shows current variables and their percentages.
3.If you try to plot with invalid data (e.g., non-numeric percentage or percentage outside 0-100), an error dialog will appear.

## How it works (High-level)
- The app maintains two lists:
- `variables`: list of variable names
- `percents`: corresponding list of percentages
- When you add a variable, the code validates the percentage and updates the in-app PrettyTable display.
- The pie chart is drawn using matplotlib's plt.pie with labels and autopct formatting.
- If the sum of percentages is less than 100, the code appends an "Другие" segment to complete the circle for visualization.

## Customization
- Theme: The app uses a forest-dark theme loaded from Forest-ttk-theme-master/forest-dark.tcl. Ensure this Tcl theme file is present or replace with your own theme:
- You can remove theme loading or switch to the default Tkinter theme.
- Labels and text: All user-facing strings are in Russian. You can translate or adjust to your preferred language.

## Validation:
- Currently enforces 0 <= percent <= 100. You can modify add_variable to customize validation rules.
- Plot behavior:
- The pie chart is titled with the input from the "Название круга" field. Update as needed.

## Project structure (example)
- main.py (or the script containing FinancialCircleApp)
- Forest-ttk-theme-master/forest-dark.tcl (optional theme)

## Troubleshooting
- If the pie chart window doesn't appear, ensure matplotlib is installed and there are no errors in the input data.
- If the PrettyTable display doesn’t refresh, verify that the circle_sys label is being updated after each addition or after clearing.

## Contributing
- Open an issue or submit a pull request to improve features, fix bugs, or add new visual themes.
- Consider adding unit tests for the data handling functions (e.g., percentage validation, "Other" slice logic).


