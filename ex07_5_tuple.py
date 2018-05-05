tuple_a = (3, 1, 2, 4)
tuple_b = (5, 7, 6, 8)

tuple_c = tuple_a + tuple_b
tuple_d = tuple(sorted(tuple_c))
print('a =', tuple_a)
print('b =', tuple_b)
print('c =', tuple_c)
print('d =', tuple_d)
print('d[3] = ', tuple_d[3])
print('3 phần tử cuối của tuple d', tuple_d[(len(tuple_d) - 3): len(tuple_d)])
