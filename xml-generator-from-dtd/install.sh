echo "Make sure python3 and pip3 are installed correctly on your system"
pip3 install -r requirements.txt
cur_dir=$(pwd)
cd src/front_end
ln -sfn $cur_dir/static
echo "Please execute run.sh and load 127.0.0.1:5000 in your browser to start the project"
