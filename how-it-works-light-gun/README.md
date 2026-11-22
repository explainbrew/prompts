# How it works: how the NES light gun "shot" the duck (it never did)

Episode 3 of "How ___ actually works". The light gun many of us knew as the NES Zapper (or, in Ukraine and Russia, the "Dendy" gun). Everything here comes from hardware write-ups, the NESdev wiki and the patent (sources at the bottom).

## It can't shoot. It can only see.

- The gun has only **two working parts**: a trigger switch and a light sensor (a photodiode behind a lens in the barrel) ([hackaday.io](https://hackaday.io/project/203034-how-the-nes-zapper-really-works/details), [nicole.express](https://nicole.express/2023/bang-bang-youre-dead.html)).
- It does **not** know where it points. The game works out the hit from what it draws on the screen.

## Black frame, then a white box

- When you pull the trigger, the game turns the whole screen **black for one frame**. On the next frame the screen is black with **one white box over the target**, one target per frame, never two boxes at once ([Wikipedia](https://en.wikipedia.org/wiki/NES_Zapper), [Hackaday](https://hackaday.com/2015/11/16/resurrecting-duckhunt)).
- The sensor only answers one question: light, or no light? Light during the box frame = hit ([NESdev wiki](https://www.nesdev.org/wiki/Zapper)).
- The black frame is a cheat check: if the sensor sees light while the screen is black, you're aiming at a lamp, not the TV.

## Why a light bulb doesn't fool it

- An NTSC TV draws 60 frames a second, 262 lines each, about 63.6 µs per line, so the beam sweeps lines about 15,700 times a second ([NESdev wiki](https://www.nesdev.org/wiki/Zapper)).
- A filter in the gun is tuned to that ~15 kHz flicker of the scanning beam, so it reacts to changes in brightness, not to brightness itself. Steady light, or a bulb's 100–120 Hz flicker, is filtered out ([nicole.express](https://nicole.express/2023/bang-bang-youre-dead.html), [NESdev wiki](https://www.nesdev.org/wiki/Zapper); the receiver circuit is in [US 4,813,682](https://patents.google.com/patent/US4813682A/en)).

## Why it's dead on a flat screen

- LCD and OLED TVs buffer the picture before showing it, so the white box arrives frames late, after the game has stopped checking.
- And there is no scanning beam, so nothing flickers for the filter to catch ([NESdev wiki](https://www.nesdev.org/wiki/Zapper), [nicole.express](https://nicole.express/2023/bang-bang-youre-dead.html)).

## Sources

- [How the NES Zapper really works](https://hackaday.io/project/203034-how-the-nes-zapper-really-works/details) (hackaday.io)
- [Bang bang, you're dead](https://nicole.express/2023/bang-bang-youre-dead.html) (nicole.express, 2023)
- [Zapper](https://www.nesdev.org/wiki/Zapper) (NESdev wiki)
- [NES Zapper](https://en.wikipedia.org/wiki/NES_Zapper) (Wikipedia)
- [Resurrecting Duck Hunt](https://hackaday.com/2015/11/16/resurrecting-duckhunt) (Hackaday, 2015)
- [US 4,813,682](https://patents.google.com/patent/US4813682A/en): the light-receiver circuit (1989)

## How the video was made

A paper collage of real photos, animated in code. Maker logos are covered; the duck is our own paper cut-out and no game graphics are shown. Photos: Evan-Amos (PD), Science Museum UK (CC BY 4.0), grmwnr (CC BY-SA 3.0), Nzeemin (CC BY 3.0), EvanProdromou (CC BY-SA 4.0), Robert Wiedemann (CC0), via Wikimedia Commons. The black frame in the opener is our own edit (one frame), not a capture of the game. Voice: AI.

**Your product, explained like this?** Email us: **hi@explainbrew.com**

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short "How the NES light gun 'shot' the duck", Nov 2026. Facts checked Nov 22, 2026. Not affiliated with Nintendo; Zapper and NES are trademarks of their owners.
