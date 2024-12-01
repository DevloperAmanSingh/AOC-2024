import os
from aocd import get_data, submit

def fetch_input(day, year=2024, input_dir="inputs"):
    """
    Fetch input for a specific day and save it to the inputs folder.
    """
    os.makedirs(input_dir, exist_ok=True)
    input_file = os.path.join(input_dir, f"day-{day:02}.txt")
    if not os.path.exists(input_file):
        print(f"Fetching input for Day {day}...")
        data = get_data(day=day, year=year)
        with open(input_file, "w") as f:
            f.write(data)
        print(f"Input saved to {input_file}.")
    else:
        print(f"Input for Day {day} already exists.")
    return input_file

def fetch_all_inputs(start_day=1, end_day=25, year=2024, input_dir="inputs"):
    """
    Fetch inputs for all days in the given range and save them.
    """
    os.makedirs(input_dir, exist_ok=True)
    for day in range(start_day, end_day + 1):
        fetch_input(day, year, input_dir)

def create_solution_file(day, solution_dir="solutions"):
    """
    Create a solution file for a specific day with a standard template.
    """
    os.makedirs(solution_dir, exist_ok=True)
    file_path = os.path.join(solution_dir, f"day-{day:02}.py")
    
    if os.path.exists(file_path):
        print(f"Solution file for Day {day} already exists: {file_path}")
        return

    template = f"""\"\"\"Solution for Advent of Code - Day {day}\"\"\"

def solve_part_1(input_data):
    \"\"\"
    Solve Part 1 of the challenge for this day.
    \"\"\"
    # TODO: Implement Part 1 solution
    return None

def solve_part_2(input_data):
    \"\"\"
    Solve Part 2 of the challenge for this day.
    \"\"\"
    # TODO: Implement Part 2 solution
    return None

# Optional: Add helper functions if needed
"""
    with open(file_path, "w") as f:
        f.write(template)
    print(f"Created solution file: {file_path}")

def submit_solution(day, part, result):
    """
    Submit the solution for a specific day and part to Advent of Code.
    :param day: The day of the challenge.
    :param part: Part 1 or Part 2.
    :param result: The result to submit.
    """
    try:
        submit(result, day=day, part=part)
        print(f"[bold green]Successfully submitted Part {part} for Day {day}: {result}[/]")
    except Exception as e:
        print(f"[bold red]Error while submitting Day {day}, Part {part}: {e}[/]")