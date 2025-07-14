from flask import Flask, jsonify
import random

app = Flask(__name__)

# Define snakes and ladders
snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

player_position = 0

@app.route('/roll', methods=['GET'])
def roll_dice():
    global player_position
    dice = random.randint(1, 6)
    next_pos = player_position + dice
    if next_pos > 100:
        return jsonify({"position": player_position, "dice": dice, "message": "Roll exceeds 100"})

    if next_pos in snakes:
        final_pos = snakes[next_pos]
        msg = f"Oops! Bitten by snake 🐍 from {next_pos} to {final_pos}"
    elif next_pos in ladders:
        final_pos = ladders[next_pos]
        msg = f"Yay! Climbed ladder 🪜 from {next_pos} to {final_pos}"
    else:
        final_pos = next_pos
        msg = "Moved normally"

    player_position = final_pos
    return jsonify({
        "position": player_position,
        "dice": dice,
        "message": msg
    })

@app.route('/reset', methods=['GET'])
def reset_game():
    global player_position
    player_position = 0
    return jsonify({"message": "Game reset", "position": 0})

if __name__ == '__main__':
    app.run(debug=True)
