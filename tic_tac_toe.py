from ttt.game_runner import GameRunner


def main(runner=GameRunner()):
    game_in_progress = True
    #
    while game_in_progress:
        runner.play_turn()
        if runner.is_game_over():
            runner._render_board()
            game_in_progress = False


if __name__ == '__main__':
    main()

