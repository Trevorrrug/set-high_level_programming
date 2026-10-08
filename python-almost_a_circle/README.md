# Almost a Circle

This project implements reusable geometric models in Python. `Base` manages
object IDs and JSON/CSV serialization. `Rectangle` validates dimensions and
positions, and `Square` extends `Rectangle` with a shared side length. The base
class also includes a Turtle drawing helper.

## Run the tests

From this directory, run:

```sh
python3 -m unittest discover tests
python3 -m pycodestyle models tests
```
