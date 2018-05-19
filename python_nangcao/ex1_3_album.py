from ex1_3_album_lib import DiaCD

i = 1
list_album = []
total = 0
while i == 1:
    name = input('Nhập tên đĩa CD: ')
    artist = input('Nhập tên ca sỹ: ')
    number = int(input('Nhập số bài hát: '))
    price = eval(input('Nhập giá thành: '))
    album = DiaCD(name, artist, number, price)
    list_album.append(album)
    for item in list_album:
        print(DiaCD.in_danhsach(item))
        total += item.price
    print('Tổng tiền:', total)
    i = int(input('Tiếp tục: 1 , Không :0 \t'))