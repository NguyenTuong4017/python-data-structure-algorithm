import ctypes

s = "tuong"
print("Initial memory address of s: ", hex(id(s)))

x = ctypes.create_string_buffer(b"tuong", 1000)
print("Initial memory address of x: ", hex(id(x)))

print(x)

s += " nguyen"
x.value += b" nguyen"

print("Final memory address of s: ", hex(id(s)), s)
print("Final memory address of x: ", hex(id(x)), x)
