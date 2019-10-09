from ttt.players.player import Player


class SmartComputerPlayer(Player):
    def __init__(self, name, marker, console):
        super().__init__(name, marker, console)
        self._game = None
        self._this_player_marker = None
        self._opponent_marker = None

    def get_move(self, game):
        return self._find_best_move(game)

    def _find_best_move(self, game):
        self._set_fields(game)
        board = game.get_board()
        best_move = None
        best_score = -100

        for move in board.available_spaces():
            new_board = board.place_marker(move, self._this_player_marker)

            score = self._minimax(new_board, self._opponent_marker)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def _set_fields(self, game):
        self._game = game
        self._rules = game.get_rules()
        self._this_player_marker = game.get_current_player_marker()
        self._opponent_marker = game.get_opponent_marker()

    def _minimax(self, board, next_marker):
        score = self._get_score(board)
        if score is not None:
            return score

        if next_marker == self._this_player_marker:
            return self._maximise(board, next_marker)
        else:
            return self._minimise(board, next_marker)

    def _get_score(self, board):
        if self._rules.is_won(board, self._this_player_marker):
            return 1
        elif self._rules.is_won(board, self._opponent_marker):
            return -1
        elif board.is_full():
            return 0

    def _maximise(self, board, marker):
        max_score = -100
        for move in board.available_spaces():
            new_board = board.place_marker(move, marker)
            score = self._minimax(new_board, self._opponent_marker)
            if score > max_score:
                max_score = score
        return max_score

    def _minimise(self, board, marker):
        min_score = 100
        for move in board.available_spaces():
            new_board = board.place_marker(move, marker)
            score = self._minimax(new_board, self._this_player_marker)
            if score < min_score:
                min_score = score
        return min_score
