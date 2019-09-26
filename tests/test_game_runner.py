from ttt.game_runner import GameRunner


class MockGame():
    def func(self):
        return None


def test_returns_a_game():
    game = MockGame()
    runner = GameRunner(game)
    assert runner.get_game() == game