s = input ('s = ')
s_sub = input ('s_sub = ')
s_find = input ('s_find = ')
s_replace = input ('s_replace = ')

print ('s: ', s)
print ('s_strip: ', s.strip(' '))
s = s.strip(' ')
print ('s_capitalized: ', s.capitalize())
print ('Số lần %s xuất hiện trong %s:' %(s_sub, s),s.count(s_sub))
print ('Chuỗi s sau khi tìm và thay: ',s.replace(s_find,s_replace))