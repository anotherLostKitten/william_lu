# William Lu

DJ Perl Module Theodore Peters, Ivan Zhang, Imad Belkebir, Adil Gondal, Honorary Memeber William Lu

An app to tell you weather you'll see pokemon -- and which ones!
Users can find info on the types of pokemon they will see based on weather conditions in their area, and be able to get further information about both the weather and the Pokemon.

The project uses OpenWeatherMap API, which requires and API key, and PokeAPI, which does not.

To aquire an API key for OpenWeatherAPI, go here.

Then, in `util/apy.py`, change the value of `weatherkey` to your API key.

After cloning, the app needs to be run from a *Python 3* virtual enviornment with *Wheel* and *Flask*. Run these commands in terminal while in the root directory of the cloned repository:

`python3 -m venv h/`

`. h/bin/activate`

`pip install -r requirements.txt`

`python appy.py`

And when done,

`deactivate`
