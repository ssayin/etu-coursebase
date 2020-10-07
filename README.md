# etu-coursebase
![ci](https://github.com/ssayin/etu-coursebase/workflows/ci/badge.svg)

CLI for ETU Coursebase

## How to use

```sh 
# cd into local repo
cd etu-coursebase
# create a virtual environment
virtualenv venv
# switch to venv
. venv/bin/activate
# install
pip install .
```
Create a json file named **config.json** in ~/.config/coursebase/ with content similar to the one below.
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

```sh 
# run
coursebase
```
## License
[BSD](LICENSE)
