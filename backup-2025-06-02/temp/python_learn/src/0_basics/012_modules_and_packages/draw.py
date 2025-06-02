def draw_game(result):
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    print(result)
    print("draw game")


def clear_screen(screen):
    print("clear screen")


class Screen:
    pass


# initialize main_screen as a singleton
main_screen = Screen()
