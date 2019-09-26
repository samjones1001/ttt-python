from ttt.game_runner import GameRunner


def main():
    game_in_progress = True
    runner = GameRunner()

    while game_in_progress:
        runner.play_turn()
        if runner.is_game_over():
            runner._render_board()
            game_in_progress = False
            return runner.get_game().get_board_state()


if __name__ == '__main__': main()