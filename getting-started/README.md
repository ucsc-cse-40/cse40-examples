# Getting Started

This example describes some of the steps you need to do to get started with the tools you will use in CSE 40.
Refer to HO0 for more information on setting up your development environment,
this exercise just covers the "how" but HO0 also talks about the "why".

## Virtual Environments

For a reference on virtual environments,
see [this guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment).

Make sure your have created your virtual environment:
```sh
python3 -m venv ~/cse40_venv
```
This example assumes that your venv is called `cse40_venv` and is located in your home directory (`~`).

Activate your venv:
```sh
source ~/cse40_venv/bin/activate
```

When you are done with the venv, you can deactivate it:
```sh
deactivate
```
You can also just close your shell/terminal and open a new one.

## Installing Python Dependencies

Make sure your venv is activated before doing any pip commands.

All dependencies for this course are declared in the `ucsc-cse40` package,
so you only need to install that:
```sh
pip3 install ucsc-cse40
```

You can also install dependencies that are listed in a requirements file using the `-r` option:
```sh
pip3 install -r requirements.txt
```
If you look inside the `requirements.txt` file in this example,
you will see that `ucsc-cse40` is the only dependency.

Once installed, you can see all the packages now installed in your venv using the `pip3 list` command:
```sh
pip3 list
```

## Starting Jupyter Lab

Note that Jupyter Lab is amongst the packages listed by the previous command:
```sh
pip3 list | grep jupyterlab
```

Now you can launch Jupyter Lab (make sure your venv is activated):
```sh
jupyter lab
```

This should open up Jupyter Lab in a web browser.
If not, directions should be printed in the terminal.

In the file explorer on the left side of the screen,
you should see the `getting-started.ipynb` file in this directory.
Double click that file to open it,
the rest of this example will be located in there.
