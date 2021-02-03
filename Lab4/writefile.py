numbers = ['one', 'two', 'three']
try:
    with open('number.txt','w') as number_file: #add to file using append 'a' for 'w'
        for n in numbers:
            number_file.write(n + '\n')
except OSError:
    print('Error writing to file. ')
