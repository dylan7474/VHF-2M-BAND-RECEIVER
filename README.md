# VHF-2M-BAND-RECEIVER

https://dylan7474.github.io/VHF-2M-BAND-RECEIVER/

A radio-style front end for listening to the UK 2 metre amateur band (144–146 MHz)
live, through volunteer-run [OpenWebRX](https://www.openwebrx.de/) receivers.

The page doesn't receive anything itself. Picking a channel or turning the knob
reloads an embedded OpenWebRX receiver tuned to that frequency
(`https://receiver/#freq=145500000,mod=nfm`).

- **Receivers:** four UK receivers that allow embedding (HTTPS, no
  `X-Frame-Options`), plus a list of HTTP-only ones that open in a new tab.
  Found via [ReceiverBook](https://www.receiverbook.de/map).
- **Channels:** the key UK band-plan frequencies, and every UK 2m repeater from
  [ukrepeater.net](https://ukrepeater.net/) (RSGB ETCC), sorted by distance
  from the chosen receiver.
- **Controls:** MEM/VFO tuning, step, mode and squelch are passed to the
  receiver. Volume is on the receiver itself.

Receivers are shared: each can only be on one band at a time, so if one is
showing another band, pick its 2m profile from its own menu.

## Updating the repeater list

```sh
python3 tools/update-repeaters.py   # rewrites repeaters.js
```
