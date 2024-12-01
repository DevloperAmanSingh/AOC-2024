import importlib
from utils import fetch_input, fetch_all_inputs, create_solution_file,submit_solution
from rich.console import Console

console = Console()

def run_day(day):
    """
    Run solutions for the specified day.
    """
    input_file = fetch_input(day)
    try:
        module = importlib.import_module(f"solutions.day-{day:02}")
        with open(input_file, "r") as f:
            input_data = f.read()

        console.print(f"[bold green]Running solutions for Day {day}...[/]")
        result_part_1 = module.solve_part_1(input_data)
        result_part_2 = module.solve_part_2(input_data)

        console.print(f"[bold blue]Part 1:[/] {result_part_1}")
        console.print(f"[bold blue]Part 2:[/] {result_part_2}")
    except ModuleNotFoundError:
        console.print(f"[bold red]Error: No solution file found for Day {day}. Creating one...[/]")
        create_solution_file(day)
    except Exception as e:
        console.print(f"[bold red]Error while running Day {day} solutions: {e}[/]")

if __name__ == "__main__":
    console.print("[bold yellow]Advent of Code Runner[/]")
    console.print("[italic]Choose an option:[/]")
    console.print("[1] Fetch input for a day")
    console.print("[2] Fetch inputs for a specific range of days")
    console.print("[3] Create a solution file for a day")
    console.print("[4] Run solutions for a specific day")
    console.print("[5] Submit solutions for a specific day")
    
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            day = int(input("Enter the day number (1-25): "))
            fetch_input(day)
        elif choice == 3:
            day = int(input("Enter the day number (1-25): "))
            create_solution_file(day)
        elif choice == 4:
            day = int(input("Enter the day number (1-25): "))
            run_day(day)
        elif choice == 2:
            start_day = int(input("Enter the start day (1-25): "))
            end_day = int(input("Enter the end day (1-25): "))
            if 1 <= start_day <= end_day <= 25:
                fetch_all_inputs(start_day=start_day, end_day=end_day)
            else:
                console.print("[bold red]Error: Invalid day range.[/]")
        elif choice == 5:
            day = int(input("Enter the day number (1-25): "))
            part = int(input("Enter the part number (1 or 2): "))
            result = int(input("Enter the result: "))
            submit_solution(day, part, result)
        else:
            console.print("[bold red]Invalid choice. Please select 1, 2, 3, or 4.[/]")
    except ValueError:
        console.print("[bold red]Invalid input. Please enter a valid number.[/]")