from fastapi import FastAPI
from fastapi.responses import JSONResponse
from train import rps

app = FastAPI()

state = (0, 0)


@app.post("/play")
async def play(player_action: int):
    global state
    if player_action not in [0, 1, 2]:
        return JSONResponse(
            {"error": "Invalid move! Please enter 0, 1, or 2."}, status_code=400
        )

    opponent_action = rps.get_action(state)
    if player_action == opponent_action:
        result = "It's a tie!"
        reward = 0
    elif (
        (player_action == 0 and opponent_action == 1)
        or (player_action == 1 and opponent_action == 2)
        or (player_action == 2 and opponent_action == 0)
    ):
        result = "You lose!"
        reward = -1
    else:
        result = "You win!"
        reward = 1

    print(result, reward)
    next_state = (opponent_action, player_action)
    rps.update_q_table(state, player_action, reward, next_state)
    state = next_state

    response = {"result": result, "reward": reward, "state": state}
    return response
