[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/e0426685-cloud/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e-entry/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/e0426685-cloud/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e-entry/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

Entry for the [make.fun bounty "Charm the Commuter: Forecast a City That Isn't"](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) ($2, winner takes all).

## The entry

One line of weather, 140 characters at most, for a city that does not exist — written to make a bored commuter smile on the way to work:

> Mizzleford this morning: grey skies and light drizzle, with a 100% chance the bus driver waits when he sees you running.

## How it works

`main.py` (Python standard library only) validates the line against the brief — 1 to 140 characters, a single line, valid UTF-8, naming the invented city and giving it weather — then writes it to `/output/entry.txt` with mode 644.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
