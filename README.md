# akttym - AKA **A**dd **c**urrent **t**rack **t**o **y**our **m**usic library

Akttym is a script which combined with global keyboard shortcut allows to add currently plaing track to "your music" section in Spotify, headlessly.

And yes, there is a typo in title.

## Getting Started

This script is written in python, so it probably works in most Linux distros and MacOS. I have'nt test it out on Windows, however, I bet there would be problem with filesystem related stuff.

Disclaimer: It only works with on-line playback.

## Usage

1. To install akttym, just simply pip install it from PyPI:

```
python3 -m pip install akttym
```

2. It comes with empty `config.yaml`. In order to fill up it with data, run `akttym` for the first time, and it will tell you where the config file is located:
```
python3 -m akttym
WARNING:root:Config is invalid. username key is empty or does not exist.
                   Config file can be found at: /Users/evemorgen/Desktop/akttym/akttym/config.yaml
```
3. Create app at <https://developer.spotify.com>, copy `client_id` and `client_secret` into config file.
4. Add `http://localhost` redirect uri your new spotify app [Edit Settings -> Redirect URIs -> ADD]
5. Run the script once again. This time it should open a website in your browser. Follow displayed istructions (accept spotify stuff and copy link that was just open, after agreeing to sell your soul, to terminal window).
6. After that, everything should work just fine.

```
python3 -m akttym
INFO:root:added Life On Mars? - 2015 Remastered Version to evemorgen's library
```

## Binding akttym with keyboard shortcut

### MacOS
1. Search for `Automator` and open it. 
2. Create new service [Service -> Choose]
3. Drag and drop `run shell script` to workflow window
4. Select `no input` in `Service receives` dropdown and fill in command textbox with `python3 -m akttym`
5. Save created service (`Cmd+S` or [File -> Save]) with name `akttym`
6. Close Automator and navigate to keyboard shortcuts settings [System preferences -> Keyboard -> Shortcuts -> Services]. At the very bottom of services list you should see newly created service. Double click on it and pick any key combination you like (be aware that you could override any of existing shortcuts)
7. Test it out? Profit?

### Ubuntu
comming soon

## Authors

* **Patryk Galczynski** - [evemorgen](https://github.com/evemorgen)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
