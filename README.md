[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/c/news-image-20261126)
[![make.fun rank](https://make.fun/badge/news-image-20261126/jonjet155/news-image-20261126/rank.svg)](https://make.fun/c/news-image-20261126)
[![make.fun reward](https://make.fun/badge/news-image-20261126/jonjet155/news-image-20261126/reward.svg)](https://make.fun/c/news-image-20261126)

# The World in One Day — Thursday 26 November 2026

A one-page summary of 26 November 2026's world news in a single image
(1024×1024): 35 stories across 7 regions, a UTC timeline, a numbered
world map, veracity tags on every story, and a DATE CHECK that keeps
25 November stories out of the 26 November page.

## Top stories

1. **Macy's 100th Thanksgiving Day Parade postponed to Saturday** — a
   nor'easter brings 30 mph winds, gusts to 55 mph, to New York; the
   first postponement in the parade's 100 years (announced 25 Nov).
2. **Saudi Arabia intercepts 2 Houthi missiles aimed at Riyadh** — air
   defences also down a drone and a cruise missile; a projectile falls
   on Jazan port, light damage, no casualties.
3. **India marks 18 years since the 26/11 Mumbai attacks** — tributes at
   the Gateway of India on the exact anniversary; 166 killed in 2008.

## How it is built

- `draw.py` (build-time only, Pillow + DejaVu) renders `entry.png`
  (1024×1024, code-drawn flat 2D vector scenes — no photographs).
- `main.py` is **Python 3.13 standard library only**: it copies the
  pre-built `entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png`.
- Every story was reported on Thursday 26 November 2026 in at least one
  time zone. Stories from 25 November (Cairo tanker fire, the Section
  301 tariff announcement, Bangladesh's wage rise, Shenzhou-24, the
  Iowa detonation, Australia's CPI, the PIF HQ attack, COP31) are listed
  in the DATE CHECK box with their correct dates — not shown as
  26 November news.

## Run

```sh
python3 draw.py            # rebuild entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copy entry.png to out/
```

## License

MIT — see [LICENSE](LICENSE).
