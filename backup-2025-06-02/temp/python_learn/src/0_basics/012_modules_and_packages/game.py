import draw


def play_game():
    print("play game")
    return "result from play game"


def main():
    result = play_game()
    draw.draw_game(result)


if __name__ == "__main__":
    main()
