conda create -n llama python=3.12 -y
conda activate llama
pip install torch 
cd llama_repo/
pip install -e .
