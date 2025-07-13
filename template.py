import os
import logging
from pathlib import Path

files = [
    "main.py",
    "agents/build_agent.py",
    "agents/deploy_agent.py",
    "agents/monitor_agent.py",
    "agents/workflow_agent.py",
    "tools/jenkins_tools.py",
    "tools/terraform_tools.py",
    "tools/kube_tools.py",
    "tools/utils.py",
    "terraform/main.tf",
    "terraform/variables.tf",
    "terraform/outputs.tf",
    "prompts/build_prompt.txt",
    "prompts/deploy_prompt.txt",
    "logs/run.log"
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")