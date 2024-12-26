from pathlib import Path
import subprocess

output_file = "README.md"

problems = {}
unique_problem_numbers = set()

git_tracked_files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()

git_tracked_files = set(git_tracked_files)

for file in Path(".").iterdir():
    if file.is_file() and file.name[0].isdigit() and file.name in git_tracked_files:
        parts = file.name.split(".")
        if len(parts) >= 3:
            problem_number = parts[0]
            problem_name = parts[1]
            lang = parts[-1]
            key = f"{problem_number}.{problem_name}"
            unique_problem_numbers.add(problem_number)
            if key not in problems:
                problems[key] = set()
            problems[key].add(lang)

sorted_problems = sorted(problems.items(), key=lambda x: int(x[0].split(".")[0]))

with open(output_file, "w") as f:
    f.write(f"{len(unique_problem_numbers)} solved\n\n")
    for problem, languages in sorted_problems:
        lang_list = ", ".join(sorted(languages))
        f.write(f"{problem} [{lang_list}]  \n")
