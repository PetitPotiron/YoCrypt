import yocrypt

number_of_tests = 3

if yocrypt.decode(yocrypt.encode('hello my name is john doe')) == 'hello my name is john doe':
    print(f'Test 1/{number_of_tests} passed')
else:
    print(f'Test 1/{number_of_tests} [ERROR]')

if yocrypt.encode('hello my name is john doe') == 'hello ud zmbm ne vdps pat':
    print(f'Test 2/{number_of_tests} passed')
else:
    print(f'Test 2/{number_of_tests} [ERROR]')

if yocrypt.decode('hello ud zmbm ne vdps pat') == 'hello my name is john doe':
    print(f'Test 3/{number_of_tests} passed')
else:
    print(f'Test 3/{number_of_tests} [ERROR]')