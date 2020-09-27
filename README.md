# etu-coursebase
CLI for ETU Coursebase

## How to use

```sh # cd into local repo
cd etu-coursebase
# create a virtual environment
virtualenv venv
# switch to venv
. venv/bin/activate
# install
pip install .
# fetch course data (one time only)
coursebase generate
```
Create json file named courses.json with content similar to the one below.
```json
{
  "lookFor": [
    "ELE 273",
    "İKT 313",
    "TAR 101",
    "İDE 218",
    "MAT 441"
  ]
}
```

```sh # run

```
## License
[BSD 3](LICENSE)
