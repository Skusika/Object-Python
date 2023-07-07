# class Song:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist
#
# class Playlist:
#     def __init__(self):
#         self.songs = []
#
#     def __getitem__(self, index):
#         return self.songs[index]
#
#     def __setitem__(self, value, song):
#         if 0 <= value <= len(self.songs):
#             self.songs.insert(value, song)
#         elif value > len(self.songs):
#             diff = value - len(self.songs)
#             self.songs.extend([0] * diff)
#             self.songs[value] = song
#
#     def add_song(self, pesnya):
#         self.songs.append(pesnya)
#
#
# # Ниже код для проверки методов классов Song и Playlist
# playlist = Playlist()
# assert len(playlist.songs) == 0
# assert isinstance(playlist, Playlist)
# playlist.add_song(Song("Paradise", "Coldplay"))
# assert playlist[0].title == 'Paradise'
# assert playlist[0].artist == 'Coldplay'
# assert len(playlist.songs) == 1
#
# playlist[0] = Song("Resistance", "Muse")
# assert playlist[0].title == 'Resistance'
# assert playlist[0].artist == 'Muse'
# assert playlist[1].title == 'Paradise'
# assert playlist[1].artist == 'Coldplay'
#
# playlist[1] = Song("Helena", "My Chemical Romance")
# assert playlist[1].title == 'Helena'
# assert playlist[1].artist == 'My Chemical Romance'
#
# assert playlist[2].title == 'Paradise'
# assert playlist[2].artist == 'Coldplay'
# print('Good')

class ShoppingCart:
    def __init__(self):
        self.items = dict()

    def __getitem__(self, name):
        if name in self.items:
            return self.items[name]
        else:
            return 0

    def __setitem__(self, value, count):
        if value in self.items:
            self.items[value] = count
        else:
            self.items[value] = count

    def __delitem__(self, value):
        self.items.pop(value)

    def add_item(self, value1, count1 = 1):
        if value1 in self.items:
            self.items[value1] += count1
        else:
            self.items[value1] = count1

    def remove_item(self, value2, count2=1):
        if value2 in self.items:
            if self.items[value2] <= count2:
                self.items.pop(value2)
            else:
                self.items[value2] -= count2



# Create a new shopping cart
cart = ShoppingCart()

# Add some items to the cart
cart.add_item('Apple', 3)
cart.add_item('Banana', 2)
cart.add_item('Orange')

assert cart['Banana'] == 2
assert cart['Orange'] == 1
assert cart['Kivi'] == 0

cart.add_item('Orange', 9)
assert cart['Orange'] == 10

print("Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

cart['Apple'] = 5
cart['Banana'] = 7
cart['Kivi'] = 11
assert cart['Apple'] == 5
assert cart['Banana'] == 7
assert cart['Kivi'] == 11

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")

# Remove an item from the cart
cart.remove_item('Banana')
assert cart['Banana'] == 6

cart.remove_item('Apple', 4)
assert cart['Apple'] == 1

cart.remove_item('Apple', 2)
assert cart['Apple'] == 0
assert 'Apple' not in cart.items

cart.remove_item('Potato')

del cart['Banana']
assert cart['Banana'] == 0
assert 'Banana' not in cart.items

print("Updated Shopping Cart:")
for item_name in cart.items:
    print(f"{item_name}: {cart[item_name]}")



