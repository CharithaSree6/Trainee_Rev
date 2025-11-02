# Convert CamelCase to snake_case

text = "CamelCaseToSnakeCase"
snake_case = ""

for char in text:
    if char.isupper():
        if snake_case != "":
            snake_case += "_"
        snake_case += char.lower()
    else:
        snake_case += char

print(snake_case)