"""
Entry script to upload the latest trained model to roboflow.
"""
import re
import os
import roboflow
from utils import resolve_latest_trained_dir
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    export_dir = resolve_latest_trained_dir()
    version_number = re.search(r'\.v(\d+)i\.', export_dir).group(1)

    rf = roboflow.Roboflow(api_key=os.getenv("RF_API_KEY"))
    workspace = rf.workspace(os.getenv("RF_WORKSPACE_ID"))
    project = workspace.project(os.getenv("RF_PROJECT_ID"))
    version = project.version(version_number)

    version.deploy("yolov8-seg", export_dir)
