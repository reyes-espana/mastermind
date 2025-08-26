# Mastermind 🧠
A Command Line implementaion of the mastermind game.

### How To Play
The game will prompt you to choose a difficulty level (1-4). You will then have 10 attempts to guess the correct number combination by using the feedback given. 

Feedback: 
* **Correct:** The correct number is in the correct position.
* **Close:** The correct number is in the wrong position.

If you successfully crack the code, you may advance to the next difficulty level. If not, you will be given the option to play again. 

### How to Run
1. To run the game, ensure you have the lastest version of [python](https://www.python.org/downloads/) installed.

1. Clone the git repository by running the following command:
    ```
    git clone https://github.com/reyes-espana/mastermind.git
    ```

1. Install the required libraries by running the following command from your terminal:
    ```
    pip install -r requirements.txt
    ```

1. From the `mastermind/` directory run the following command:
    ```
    python src/mastermind.py
    ```

## File Structure
This project is organized into several key directories to separate logic and improve maintainability.
### `src/`
The main application directory, containing the primary game logic.

### `app/`
Integrates the services into a simplified and accessible file.

### `services/`
This directory contains the core logic for the game, with each file focused on a specific function:
* `generate.py`:
    * Handles number generation, either locally or via the [Random.org API](https://www.random.org/integers).
* `response.py`:
    * Manages user-facing feedback and messages.
* `stats.py`:
    * Contains the algorithm for scoring a user's guess and providing feedback.
* `user.py`:
    * Manages all functions related to user input.
* `validate.py`:
    * Validates user input to ensure it meets game requirements.

### `db/`
Handles all database interactions for the game, such as storing game stats or high scores.
