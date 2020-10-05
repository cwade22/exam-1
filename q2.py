num_spaces = 0
while num_spaces < 30:
    print('#', end='')
    num_printed = 0
    while num_printed < num_spaces:
        print(' ', end='')
        num_printed += 1
    print('#')
    num_spaces += 1