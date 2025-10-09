def solution(csv_string):
    lines = csv_string.strip().split('\n')
    if not lines:
        return ""

    clean_lines = [lines[0]]

    for line in lines[1:]:
        fields = line.split(',')
        if 'NULL' not in fields:
            clean_lines.append(line)

    return '\n'.join(clean_lines)