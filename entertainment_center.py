import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://vignette4.wikia.nocookie.net/pixar/images/c/ca/Toy_story_ver1_xlg.jpg/revision/latest?cb=20110515142143",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

                 
spy = media.Movie("Spy",
                  "�@�ӫܷQ�������Ҫ��D�k���d���ڦV���Ҥ���",
                  "http://www.rogerogreen.com/wp-content/uploads/2015/07/spy-poster.jpg",
                  "https://www.youtube.com/watch?v=D_X7FTEcbL4")

Zootopia = media.Movie("Zootopia",
                       "�@���ߤl�Τ@�����W�p��αo�ۧڻ{�P���G��",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

finding_dory = media.Movie("Finding Dory",
                           "��@�����ܪ������G��",
                           "http://orig05.deviantart.net/5bc2/f/2015/315/d/7/finding_dory_2016_by_deztrips-d9gb5br.png",
                           "https://www.youtube.com/watch?v=3JNLwlcPBPI")

the_hangover = media.Movie("The Hangover",
                           "����|�ӤH�s��~��",
                           "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg",
                           "https://www.youtube.com/watch?v=vhFVZsk3XEs")
                       
movies = [toy_story, avatar, spy, Zootopia, finding_dory, the_hangover]
fresh_tomatoes.open_movies_page(movies)                    
print(media.Movie.valid_ratings)
print(media.Movie.__doc__)
