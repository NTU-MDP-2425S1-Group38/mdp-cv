"""
Script to train then export the model, but executed as a CLI
"""

import argparse
from utils import train_and_export


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a YOLO segmentation model.")

    parser.add_argument("-d", "--data", type=str, required=True, help="Name of the folder in /data/")
    parser.add_argument("-w", "--weight", type=str, required=True, help="Name of raw weights in /weights/raw/")
    parser.add_argument("-e", "--epochs", type=int, required=True, help="Set number of training epochs")

    args = parser.parse_args()

    train_and_export(args.weight, args.data, epochs=args.epochs)


if __name__ == "__main__":
    main()
