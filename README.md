# MDP Computer Vision

Computer vision and image recognition portion of the MDP project.

---

## Getting Started

1. Create a virtual environment

```zsh
python3.11 -m venv venv
```

> [!WARNING]
> You should be using Python 3.11, since PyTorch (and related libraries) have questionable support for 3.12.

2. Activate the environment.

```zsh
source ./venv/bin/activate
```

3. Install requirements

```zsh
pip install -r requirements.txt
```

---

## Files

Raw weights have to be placed in the following directory.

```text
/weights/raw
```

Data (exported as `yolov8` format) has to be placed in the following directory.

```text
/data/
```

---

## Training

To train (and save) the model, simply use `utils.train_and_export` to train a `yolov8` model. This function abstracts
the training function calls from Ultralytics, and model export settings. More importantly, it handles the loading of
data path and model path (which is why the files above have to be placed in the correct directories).

```python
from utils import train_and_export

train_and_export("my_weight_name.*", "name_of_data_set")
```

This will train the model and export the model and checkpoints into `/weights/trained/`.

> [!NOTE]
> See the documentation of `train_and_export`, as the number of epochs and image size can be specified.

