# Quality logs and notes

### Time started: 2020-09-01 21:37
### First part ended: 2020-09-02 02:37

### Second part started: 2020-09-02 07:09
Break: 09:30-09:55

Break: 12:45-13:10

Break: 15:00-15:40

### Time ended: ..:..

## Notes:

This was my motivation to change the file locations a little bit: 
    
    "There are two fundamental choices to make in life: accept 
    the pre-existing conditions or accept the responsibility 
    to change them." - Denis Waitley.

There was no `README.md` file in the starting file: 
`GeektasticCodeChallenge_130173_1598992719913.zip`

Created `README.md` file with instructions for how to use the application.
Created `.editorconfig` file to aid collaboration in the project.
Created `app` package and moved some application files there.
Created `tests` directory and test file for `bill_members.py` functions.

Created Sphinx documentation in `docs` folder with custom theme `sphinx-rtd-theme`.
HTML version of the documentation is available in `docs/_build/html`. 
All you need to do is to make sure requirements are installed and 
`cd` to `docs` directory and run `make html`.

Updated `load_readings.py` for handling errors with `readings.json` file.

Using `tariff.py` const `BULB_TARIFF` for bill calculations.

Create classes and their functions in `models.py`.

Calculate monthly usage.

Prepare for gas billing.
