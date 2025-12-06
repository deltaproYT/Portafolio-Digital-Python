data = ['Hello World',20, 20.5, 1j, [ 'Apple', 'Banana' , 'Cherry' ], ( 'Apple', 'Banana' , 'Cherry' ), range(10), {'name': 'John', 'Age': 36}, frozenset({ 'Apple', 'Banana' , 'Cherry' }), True, b'Hello', bytearray(5), memoryview(bytes(5)), None]
for i in range(len(data)):
    print(data[i])
    print(type(data[i]), '\n')