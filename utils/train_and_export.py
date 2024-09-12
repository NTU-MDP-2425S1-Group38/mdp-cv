"""
This file handles the training logic, and exporting of model.
"""
import os
from time import localtime, strftime

import torch
from ultralytics import YOLO
from utils import resolve_data, resolve_raw_weight, export_to_onnx


def __determine_best_device() -> str:
    """
    Function to determine the fastest running device and return the
    Ultralytics compatible name.
    :return: str {"0", "mpu", "cpu"}
    """
    if torch.cuda.is_available():
        print("Using GPU!")
        return "0"

    if torch.backends.mps.is_available():
        print("Using MPS!")
        return "mps"

    print("No hardware accelerator! Using CPU!")
    return "cpu"


def train_and_export(
        raw_weight_name:str, data_name:str,
        epochs:int=1,
        imgsz:int=640
) -> None:
    """
    Function to train then export the model.
    Used to standardise the naming convention of exported files.
    :param data_name: Folder name containing `data.yaml` in root/data
    :param raw_weight_name: Name of raw weight in /root/weights/raw
    :param epochs: Number of epochs to train the model
    :param imgsz: Size of image model to use
    :return: None

    See: https://docs.ultralytics.com/modes/train/
    """

    # Resolve files in project directory
    data_yaml_file = resolve_data(data_name)
    raw_weight = resolve_raw_weight(raw_weight_name)

    # Begin training of model
    model = YOLO(raw_weight)
    model.train(
        data=data_yaml_file,
        epochs=epochs,
        imgsz=imgsz,
        fliplr=0, flipud=0,
        project=f"{os.path.dirname(__file__)}/../weights/trained",
        name=f"model_{strftime('%Y-%m-%d_%H-%M-%S', localtime())}_EPOCHS {epochs}_{data_name}",
        device=__determine_best_device(),
        verbose=True
    )

    # Export model
    export_to_onnx(model)

