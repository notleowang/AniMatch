from login import login_anilist
from query import get_viewer

access_token = None


def main():
    global access_token
    
    while True:
        print('\nAniMatch')
        print('-----------------------')
        print('1 - Start now')
        if not access_token:
            print('2 - Login with AniList')
            print('3 - Login with MAL')
        else:
            print('4 - Recommend based off Favourites')
            print('5 - Recommend based off Trending')
            print('6 - Recommend based off Genre')
        print('q - Quit Application')
        print('-----------------------\n')
        
        x = input("Input: ")
        
        match x:
            case '1':
                continue
            case '2':
                access_token = login_anilist()
                if access_token:
                    get_viewer(access_token)
            case '3':
                # MAL discontinuing?
                continue
            case '4':
                continue
            case '5':
                continue
            case '6':
                continue
            case 'q':
                return 0


if __name__ == "__main__":
    main()
    
    