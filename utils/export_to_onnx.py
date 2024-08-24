from ultralytics import YOLO


def export_to_onnx(model: YOLO, model_format: str = "onnx") -> None:
    """
    Function to export model to Onnx, with a standardised opset and args.
    :param model: YOLO model to be exported
    :param model_format: "onnx" | "pytorch"
    :return: None
    """

    if model_format == "onnx":
        model.export(format="onnx", simplify=True, opset=19)

    if model_format == "pytorch":
        model.export()
