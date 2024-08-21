"""
Code to resolve file directory location.
"""

import os


def resolve_data(data_name:str) -> str:
    """
    Ultralytics would most likely take in the absolute path of data.yaml file. This file
    aims to resolve the path to the data.yaml file from just the name of the data
    file name.
    :param data_name: File name of dataset downloaded from Roboflow, in yolov8 format.
    :return: Absolute file path to the `data.yaml` file.
    """
    return f"{os.path.dirname(__file__)}/../data/{data_name}/data.yaml"

def resolve_raw_weight(raw_weight_name:str) -> str:
    """
    Function to return the absolute path to the raw model, located in /weights/raw/
    :param raw_weight_name: Name of weight
    :return: Absolute path to the weight
    """
    return f"{os.path.dirname(__file__)}/../weights/raw/{raw_weight_name}"
