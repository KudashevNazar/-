from rich.console import Console
from rich.table import Table

def print_table(df):
    table = Table(title="Таблиця")
    for col in df.columns:
        table.add_column(str(col))
    for _, row in df.iterrows():
        table.add_row(*[str(v) for v in row])
    Console().print(table)