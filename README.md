# Initialize Git and DVC
git init
dvc init

# Set up .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".vscode/" >> .gitignore
echo "metrics.json" >> .gitignore
echo "models/model.pkl" >> .gitignore

# Add data and model files to DVC
dvc add data/processed.csv
dvc add models/model.pkl

# Add metrics file to DVC
dvc add metrics.json

# Configure AWS S3 as a DVC remote storage
dvc remote add -d myremote s3://<your-bucket-name>/<path-to-folder>
dvc remote modify myremote access_key_id '<AWS_ACCESS_KEY_ID>'
dvc remote modify myremote secret_access_key '<AWS_SECRET_ACCESS_KEY>'
dvc remote modify myremote region '<AWS_REGION>'

# Push the DVC-tracked data to the remote storage
dvc push

# Create DVC pipeline stages in dvc.yaml
echo "
stages:
  train:
    cmd: python src/model.py data/processed.csv
    deps:
      - data/processed.csv
      - src/model.py
    outs:
      - models/model.pkl
    metrics:
      - metrics.json:
          cache: false  # Do not cache the metrics
" > dvc.yaml

# Visualize the DVC pipeline as a Directed Acyclic Graph (DAG)
dvc dag

# Run the DVC pipeline
dvc repro

# View the metrics from the output metrics.json
dvc metrics show

# Force add metrics.json to Git if it is ignored by .gitignore
git add -f metrics.json
git commit -m "Force add metrics.json to track with Git"

# Commit changes made to dvc.yaml or other DVC-tracked files
git add dvc.yaml
git commit -m "Fix metrics section format in dvc.yaml"

# Pushing data to the remote S3 bucket
dvc push

# Pull data from the remote storage (e.g., when switching branches)
dvc pull

# Add and commit all changes to Git
git add .
git commit -m "Initialize repository, add processed data and model files"

# Commit any changes made to DVC-tracked files
git add dvc.yaml
git commit -m "Update metrics section format in dvc.yaml"

# Final Git commit with changes
git commit -m "Update model and metrics"
