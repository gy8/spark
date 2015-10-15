PYTHON_INSTALL_COMMAND = """
rm -rf /tmp/hadoop-2.4.1-src* &&
sudo yum install -y python27-pip.noarch &&
sudo yum install -y gcc gcc-c++ &&
sudo yum install -y binutils &&
sudo yum install -y libgfortran atlas-sse3-devel lapack-devel &&
sudo yum install -y freetype-devel libpng-devel &&
sudo yum install -y python27-devel.x86_64 &&
sudo yum install -y postgresql94-devel &&
sudo yum install -y libxslt-devel.x86_64 &&
sudo yum install -y libxslt-python27.x86_64 &&
sudo yum install -y libxml2-python27.x86_64 &&
sudo yum install -y mysql-devel &&
sudo yum install -y libffi-devel &&
sudo yum install -y vim +ruby &&
pip-2.7 install boto &&
pip-2.7 install haversine &&
pip-2.7 install lxml &&
pip-2.7 install nameparser &&
pip-2.7 install python-dateutil &&
pip-2.7 install psutil &&
pip-2.7 install requests &&
pip-2.7 install Unidecode &&
pip-2.7 install usaddress &&
pip-2.7 install xmltodict &&
pip-2.7 install nose &&
pip-2.7 install pyzmq &&
pip-2.7 install tornado &&
pip-2.7 install ipython &&
pip-2.7 install python-Levenshtein &&
pip-2.7 install fuzzywuzzy &&
pip-2.7 install psycopg2 &&
pip-2.7 install sqlalchemy &&
pip-2.7 install probablepeople &&
pip-2.7 install numpy==1.9.3 &&
pip-2.7 install scipy &&
pip-2.7 install scikit-learn &&
pip-2.7 install pandas &&
pip-2.7 install matplotlib &&
pip-2.7 install seaborn &&
pip-2.7 install nltk &&
pip-2.7 install gensim &&
pip-2.7 install googlemaps &&
pip-2.7 install jupyter &&
pip-2.7 install python-slugify &&
pip-2.7 install phonenumbers &&
pip-2.7 install statsmodels 
"""
