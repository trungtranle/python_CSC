def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    print(f.read())
    f.close


def summarize_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines = 0
    word = 0
    char = 0
    for line in f:
        lines += 1
        word += len(line.split())
        char += len(list(line))
    print('---Summary---')
    print(lines, 'Lines \t', word, 'Words \t', char, 'Characters')
    f.close()


def write_file_once(filename):
    f = open(filename, 'w+', encoding='utf-8')
    content = input('Content: ')
    f.write(content)
    print('Written in', f.name)
    f.close()


def write_at_file_end(filename):
    f = open(filename, 'a+', encoding='utf-8')
    i = 1
    while i == 1:
        content = input('Content: ')
        f.write(content)
        i = int(input('Tiếp tục nhập: Tiếp tục: 1, Không <> 1: '))
    print('Đã ghi nội dung vào file', filename)
    f.close()
