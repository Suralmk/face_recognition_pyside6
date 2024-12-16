
# Face Recognition Pyside6

This is a face Recognition Gui app implmented in Pyside6 and QtDesigner

## Installation

Clone Repository

```bash
git clone https://github.com/Suralmk/face_recognition_pyside6.git
```

```bash 
cd face_recognition_pyside6
```

Create virtual envoiroment

```bash
python3 -m venv env
```

Activate virtual envoiroment

```bash
source env/Scripts/activate  # For Windows

source env/bin/activate  # For Linux
```

```bash
pip install -r requirements.txt
```

If you are having an issue with dlib wheel installiation, you can install by using the dlib wheel installer from dlib folder for the python verdion you are using



```bash
pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
```

```bash
python main.py
```


## Appendix

for identinfying the correct dlib installer 
if your python verion is 3.11 istall with 

```bash
pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
```

cp311 ~ python version 3.11
