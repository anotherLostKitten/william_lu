# William Lu

DJ Perl Module Theodore Peters, Ivan Zhang, Imad Belkebir, Adil Gondal, Honorary Memeber William Lu

An app to tell you weather you'll see pokemon -- and which ones!

Users can find info on the types of pokemon they will see based on weather conditions in their area, and be able to get further information about both the weather and the Pokemon.

The project uses [*OpenWeatherMap API*](https://openweathermap.org/api), which requires and API key, and [*PokeAPI*](https://pokeapi.co/), which does not.

To aquire an API key for OpenWeatherAPI, [**one must sign up**](https://home.openweathermap.org/users/sign_up).

Then, in `util/keys.txt`, paste your key in place of whatever is currently there.

After cloning, the app needs to be run from a [*Python 3*](https://docs.python.org/3/index.html) virtual enviornment with [*Wheel*](https://wheel.readthedocs.io/en/stable/) and [*Flask*](http://flask.pocoo.org/docs/1.0/). Run these commands in terminal while in the root directory of the cloned repository:

##### First time installation:

```bash
python3 -m venv h/
. h/bin/activate
pip install -r requirements.txt
deactivate
```

##### Running the app:

```bash
. h/bin/activate
python appy.py
```

And when done,

```bash
deactivate
```
