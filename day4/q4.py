with open("input4.txt") as file:
    file_text = file.read()


grid = [list(line) for line in file_text.strip().splitlines()]

def count_words_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    for i in range(rows):
        for j in range(cols - word_len + 1):
            if grid[i][j:j + word_len] == list(word):
                count += 1
                
            if grid[i][j:j + word_len] == list(word[::-1]):
                count +=1
    
    for j in range(cols):
        for i in range(rows - word_len + 1):
            if all(grid[i + k][j] == word[k] for k in range(word_len)):
                count += 1

            if all(grid[i + k][j] == word[::-1][k] for k in range(word_len)):
                count += 1

    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            j = d - i
            if j < cols:
                diagonal.append(grid[i][j])
        count += count_words_line(diagonal, word)

    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            j = cols - 1 - d + i
            if j >= 0:
                diagonal.append(grid[i][j])
        count += count_words_line(diagonal, word)

    return count

def count_words_line(line, word):
    count = 0
    line_str = ''.join(line)
    count += line_str.count(word)
    count+= line_str[::-1].count(word)
    return count


def part1():
    word = "XMAS"

    print(count_words_grid(grid,word))
    return

part1()