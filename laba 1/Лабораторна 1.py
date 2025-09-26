from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, IntPrompt
console = Console()

first_name = Prompt.ask("Введіть ім'я")
last_name = Prompt.ask("Введіть прізвище")
group = Prompt.ask("Введіть групу", choices=["КБ-101", "КБ-102", "КБ-103"],
case_sensitive=False)
variant = IntPrompt.ask("Введіть варіант")

text = Text("Інформація про студента", style="bold bright_red")
table = Table(title=text, header_style="bold bright_green")
table.add_column("Ім'я ", style="bold magenta", justify="left", no_wrap=True)
table.add_column("Прізвище ", style="italic red", justify="left")
table.add_column("Група", justify="center", style="bold #000087")
table.add_column("Варіант", justify="center", style="rgb(175,135,0)")
table.add_row(first_name, last_name, group, f"{variant}")
console.print(table, justify="center")

