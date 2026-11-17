import chess

from src.evaluate import evaluate, evaluate_breakdown


def test_evaluate_does_not_mutate_board():
    board = chess.Board()
    fen_before = board.fen()
    evaluate(board)
    assert board.fen() == fen_before


def test_starting_position_near_zero():
    board = chess.Board()
    assert abs(evaluate(board)) <= 20


def test_breakdown_has_keys():
    d = evaluate_breakdown(chess.Board())
    assert {"material", "pst", "mobility", "total"} <= set(d.keys())

