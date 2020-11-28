from Interpreter import InteractiveConsole

header = "Kevin Moy's Python Interpreter v1.0"

scope_vars = {"answer": 42}

InteractiveConsole(locals=scope_vars).interact(header)
