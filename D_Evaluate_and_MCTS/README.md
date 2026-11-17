# D 部分：评估函数与自创算法 MCTS

负责人：D  
对接人：B (后端集成)、C (搜索调用)、F (论文)

## 接口说明（给 C 和 B 看）

- `from src.evaluate import evaluate`
  - `evaluate(board: chess.Board) -> int`
  - 从当前走子方 (`board.turn`) 视角返回厘兵整数。

- `from src.mcts import choose_move`
  - `choose_move(board: chess.Board, time_limit: float = 3.0, rollout_limit: int = 20) -> chess.Move`
  - 返回合法走法，不修改传入的 `board`。

## 论文素材（给 F 看）

1. 评估函数：子力 (material) + 位置表 (PST) + 机动性 (mobility)。
2. 自创算法：MCTS，UCB1 公式，时间预算控制，rollout 步数截断。

## 约定

- 仅使用 `python-chess` 的标准 API。
- 评估函数返回值必须是整数。
- 评估和 MCTS 都不修改传入的棋盘对象。

