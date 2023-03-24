pip install jupyter_contrib_nbextensions==0.5.1
pip install plotly==5.13.1
pip install voila==0.4.0

jupyter contrib nbextension install --user
jupyter nbextension enable toc2/main

echo "c.ContentsManager.allow_hidden = True" >> /home/jovyan/.jupyter/jupyter_notebook_config.py


conda create -n py310_new python=3.10 -y
source /opt/conda/etc/profile.d/conda.sh
conda activate py310_new
pip install -r requirements_py310_new.txt

python -m ipykernel install --user --name py310_new

