from lib.models.song import Song

class CLI:

    def __init__(self):
        Song.create_table()
        self.welcome()
        self.main_menu()

    def welcome(self):
        print("//////////////Welcome to the Song Sing Place////////////////")

    def main_menu(self):
        self.show_menu()
        user_input = ""
        # while not any(item == user_input for item in ["1", "2", "3","4","5"]):
        while user_input != "5":
            # print(">>> ", end="")
            user_input = input(">>> ")
            if user_input == "1":
                self.add_song()
                self.show_menu()
            elif user_input == "2":
                # do stuff
                pass
            elif user_input == "3":
                # do stuff
                pass
            elif user_input == "4":
                # do stuff
                pass
            elif user_input == "5":
                print("Exiting....")
                print("Goodbye thanks for coming see ya later!")
            else:
                print("Invalid input please try again")
                # self.main_menu()


    def show_menu(self):
        print("Please choose an option:")
        print("1. Add Song")
        print("2. View Songs")
        print("3. Favorite Songs")
        print("4. Go back and see that amazing welcome message")
        print("5. Exit")
    
    def add_song(self):
        print("What is the name of the song you'd like to add?")
        song_name = input(">>> ")
        print("What is the artist who performed the song?")
        artist_name = input(">>> ")
        print("Is this your all time fav? (y/n)")
        favorite = input(">>> ")

        new_song = Song(song_name, artist_name, favorite)
        new_song.create()
        print(f"{new_song.name} was created and has an id of {new_song.id}")