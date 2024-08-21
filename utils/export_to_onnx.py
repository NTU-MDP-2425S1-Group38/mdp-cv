from ultralytics import YOLO

def export_to_onnx(model: YOLO) -> None:
    """
    Function to export model to Onnx, with a standardised opset and args.
    :param model: YOLO model to be exported
    :return: None
    """
    model.export(format="onnx", simplify=True, opset=19)
