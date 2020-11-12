# Queens Puzzle

Here's the programming problem: https://en.wikipedia.org/wiki/Eight_queens_puzzle

These are the different aspect of the project you can work on (in order):

- [x] Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens.
- [x] Iterate over N and store the solutions in postgres using SQLAlchemy.
- [ ] Write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest
- [x] Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
- [ ] setup Travis CI (or similar) for your public GitHub repo to run the tests automatically

## Notes:

This solution it's based on N-Queens-Puzzle implemented by Paul Silisteanu (@sol-prog).
https://github.com/sol-prog/N-Queens-Puzzle

## Requirements:

- [Docker](https://docs.docker.com/engine/installation/).
- [Docker-compose](https://docs.docker.com/compose/install).

## Install:

**Clone the repository**

```shell
git clone git@github.com:pixelead0/nQueensPuzzle.git

```

**Copy the example environment variables.**

```shell
cp .env.example .env
```

**Run docker-compose to start the containers:**

```shell
docker-compose up
```

# Run

To run use: `docker-compose exec app python puzzle_queen.py --help`

```shell
docker-compose exec app python  puzzle_queen.py --help
Usage: puzzle_queen.py [OPTIONS]

  The eight queens puzzle in Python.

Options:
  -n, --pieces INTEGER  Number of queens.
  -f, --full_board      Show solutions on full NxN board.
  -s, --short_board     Show the queens positions on the board in compressed
                        form, each number represent the occupied column
                        position in the corresponding row.

  --help                Show this message and exit.
```

# Demo:

Queens Puzzle with python example
[![asciicast](https://asciinema.org/a/372371.svg)](https://asciinema.org/a/372371)

Queens Puzzle with python - 12x12
[![asciicast](https://asciinema.org/a/372373.svg)](https://asciinema.org/a/372373)

Queens Puzzle with python - 13x13
[![asciicast](https://asciinema.org/a/372370.svg)](https://asciinema.org/a/372370)

https://asciinema.org/a/372370
