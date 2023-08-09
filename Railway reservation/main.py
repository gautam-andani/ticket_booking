from Train import Train
from Reserve import Reserve

t = Train()
app = Reserve(t)
for x in range(10):
    app.book_seat()