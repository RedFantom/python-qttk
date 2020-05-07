# qttk - tile-qt fork

## Building
This package depends on the Qt 4 header files, which are not available
on Ubuntu 20.04. The project also depends on `tk-dev` and `tcl-dev`. On
Ubuntu 18.04 and below:
```
sudo apt install tk-dev tcl-dev libqt4-dev
cmake .
make
sudo make install
```
