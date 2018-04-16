import my_media

spy = my_media.MyMovie("Spy"
                       ,"一個很想成為間諜的胖女的搞笑邁向間諜之路"
                       ,"https://www.youtube.com/watch?v=D_X7FTEcbL4")

print("電影名稱:")
print(spy.title)

print("簡介:")
print(spy.storyline)

spy.movie_trailer()
