# akttym - AKA **A**dd **c**urrent **t**rack **t**o **y**our **m**usic library

Have you ever caught yourself liking tracks on Spotify obsessively to take advantage of their sweet machine learning recommendations? Yeah, me too. But alt-tabbing into the app every 3 minutes sucks. With `akttym` you can stay focused on your work and place like on your favorite music with a keyboard shortcut.

`Akttym` is a simple script placing heart/like/whatever-they-call-it on currently playing track on Spotify, which combined with global keyboard shortcut allows for complete headless setup.

And yes, there is a typo in the name.

## Getting Started

This is a Python3 script, so it works with most Linux distributions and with macOS. I haven't tested it out on Windows, if there's a demand for it, please let me know!

Disclaimer: It only works with on-line playback.

## Usage

1. To install akttym, just simply pip install it from PyPI:

```
python3 -m pip install akttym
```

2. It comes with empty `config.yaml`. In order to fill it up with your user data, run `akttym` for the first time, and it will tell you where the config file is located:
```
python3 -m akttym
WARNING:root:Config is invalid. username key is empty or does not exist.
                   Config file can be found at: /Users/evemorgen/Desktop/akttym/akttym/config.yaml
```
3. Create a Spotify app at <https://developer.spotify.com/dashboard> and copy `client_id` and `client_secret` into config file. Don't forget to add your `username` as well.
4. Add `http://localhost:1911/` redirect uri your new spotify app [Edit Settings -> Redirect URIs -> ADD]. 
5. Run the script once again. This time it should open a website in your browser. Accept Spotify privacy stuff, after agreeing to sell your soul, you're good to go.
6. It just works! (hopefully).

```
python3 -m akttym
INFO:root:added Life On Mars? - 2015 Remastered Version to evemorgen's library
```

## Binding akttym to keyboard shortcut

### MacOS
1. Search for `Automator` app and open it. 
2. Create new service [Service -> Choose]
3. Drag and drop `run shell script` to workflow window
4. Select `no input` in `Service receives` dropdown and fill in command textbox with `python3 -m akttym`
5. Save created service (`Cmd+S` or [File -> Save]) with name `akttym`
6. Close Automator and navigate to keyboard shortcuts settings [System preferences -> Keyboard -> Shortcuts -> Services]. At the very bottom of services list you should see newly created service. Double click on it and pick any key combination you like (be aware that you could override any of existing shortcuts)
7. Test it out? Profit?

### ElementaryOS (Gnome)
1. Enter keyboard settings [System Settings -> Keyboard -> Shortcuts -> custom]
2. Click on `+` button and add `python3 -m akttym` command
3. it works?

## Troubleshooting
#### Everytime I run it, it opens a new browser tab
Try to `chmod 766 /path/to/script/dir`. Akttym needs write permission in directory where it's located

#### Browser tab opens with message `INVALID_CLIENT: Invalid redirect URI`
Make sure the right redirect uri (`http://localhost:8080/`) is added to the Spotify app.
After clicking `Add` button you still have to click `Save` button at the very bottom of the page.

## Authors

* **Patryk Galczynski** - [evemorgen](https://github.com/evemorgen)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
