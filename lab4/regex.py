import random


def generate_string(pattern: str) -> str:
    result = ""
    i = 0
    while i < len(pattern):
        char = pattern[i]
        if char == '(':
            j = i + 1
            subpattern = ""
            while pattern[j] != ')':
                subpattern += pattern[j]
                j += 1
            choices = subpattern.split('|')
            subpattern = random.choice(choices)
            repeat = 1
            i = j + 1
            if j + 1 < len(pattern):
                match pattern[j + 1]:
                    case '^':
                        if pattern[j + 2].isdigit():
                            repeat = int(pattern[j + 2])
                            i = j + 3
                    case '*':
                        repeat = random.randint(0, 3)
                        i = j + 2
                    case '+':
                        repeat = random.randint(1, 3)
                        i = j + 2
                    case '?':
                        repeat = random.randint(0, 1)
                        i = j + 2
            result += subpattern * repeat
            continue

        next_char = pattern[i + 1] if i + 1 < len(pattern) else ""
        match next_char:
            case '^':
                result += char * int(pattern[i+2])
                i += 3
                continue
            case '*':
                result += char * random.randint(0, 5)
                i += 2
                continue
            case '+':
                result += char * random.randint(1, 5)
                i += 2
                continue
            case '?':
                result += char * random.randint(0, 1)
                i += 2
                continue
            case _:
                result += char
                i += 1

    return result


def show_sequence(pattern: str):
    operations = []
    operation_number = 1
    i = 0
    while i < len(pattern):
        char = pattern[i]
        if char == '(':
            j = i + 1
            subpattern = '('
            while pattern[j] != ')':
                subpattern += pattern[j]
                j += 1
            subpattern += ')'
            operations.append(subpattern)
            if j + 1 >= len(pattern):
                break
            if pattern[j + 1] in "*+?":
                print(f"{operation_number}: {operations[-1]}")
                operations[-1] = subpattern + pattern[j+1]
                operation_number += 1
                i = j + 2
            elif pattern[j + 1] == "^":
                print(f"{operation_number}: {operations[-1]}")
                operations[-1] = subpattern + pattern[j + 1] + pattern[j + 2]
                operation_number += 1
                i = j + 3
            else:
                i = j + 1
            continue
        if i + 1 >= len(pattern):
            operations.append(char)
            i += 1
            continue
        if pattern[i + 1] in "*+?":
            operations.append(char + pattern[i + 1])
            i += 2
        elif pattern[i + 1] == "^":
            operations.append(char + pattern[i + 1] + pattern[i + 2])
            i += 3
        else:
            operations.append(char)
            i += 1

    for i in range(len(operations)):
        if len(operations[i]) > 1:
            print(f"{operation_number}: {operations[i]}")
            operation_number += 1

    operation = operations[0]
    for n in range(1, len(operations)):
        operation += operations[n]
        print(f"{operation_number}: {operation}")
        operation_number += 1


pattern1 = "(S|T)(U|V)w*y+24"
pattern2 = "L(M|N)O^3P*Q(2|3)"
pattern3 = "R*S(T|U|V)W(X|Y|Z)^2"

generated_string = generate_string(pattern1)
print("Generated string:", generated_string)
generated_string = generate_string(pattern2)
print("Generated string:", generated_string)
generated_string = generate_string(pattern3)
print("Generated string:", generated_string)

show_sequence(pattern3)


