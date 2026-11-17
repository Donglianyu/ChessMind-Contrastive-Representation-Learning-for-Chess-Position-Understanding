import chess

from src.mcts import choose_move


def test_mcts_returns_legal_move_and_does_not_mutate():
    board = chess.Board()
    fen_before = board.fen()
    move = choose_move(board, time_limit=0.2, rollout_limit=5)
    assert move in board.legal_moves
    assert board.fen() == fen_before

