from ctypes import *

# CType boolean
b0 = c_bool(0)
b1 = c_bool(1)

print(b0, b1)

print(type(b0))
print(type(b1))

print(b0.value)
print(b1.value)

# Unsigned int
i0 = c_uint(-1)
print(i0.value)

# String = char pointer
# Not mutable. So when passed to a func, the memory
# address gets changed NOT the content of that memory block
c0 = c_char_p(b"test")
print(c0.value)


p0 = create_string_buffer(5)
print(p0)
print(p0.raw)
print(p0.value)

p0.value = b"123"
print(p0)
print(p0.raw)
print(p0.value)


# Useful if the C func expects a pass by reference
i = c_int(42)
pi = pointer(i)

print(i)
print(pi)
print(pi.contents)


print(p0.value)
print(p0)
print(hex(addressof(p0)))

pt = byref(p0)
print(pt)
print(cast(pt, c_char_p).value)

# C Struct
class PERSON(Structure):
    _fields_ = [("name", c_char_p), ("age", c_int)]

bob = PERSON(b"bob", 42)
print(bob.name)
print(bob.age)


alice = PERSON(b"alice", 42)
print(alice.name)
print(alice.age)

# CTypes array/list
# you need to define the length prior
person_array_t = PERSON * 3
person_array = person_array_t()

person_array[0] = bob
person_array[1] = alice

print("------- Person Array")
for person in person_array:
    print(person.name, person.age)
