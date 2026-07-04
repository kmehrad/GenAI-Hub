conda create --name anomalyclip python=3.10 -y
conda activate anomalyclip
git clone https://github.com/zqhang/AnomalyCLIP.git AnomalyCLIP_repo
pip install -r AnomalyCLIP_repo/requirements.txt 
pip install thop ftfy regex tabulate opencv-python
pip install "numpy<2"
