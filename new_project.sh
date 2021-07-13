#!/usr/bin/env bash

PNAME=$1
BASENAME=$(basename $PNAME)
RM=$PNAME/README.md

if [ $# -ne 1 ]; then
    echo "Project needs a name"
    exit 1
fi

echo "Building directory structure..."
mkdir $PNAME
mkdir $PNAME/bin
mkdir $PNAME/data
mkdir $PNAME/doc
mkdir $PNAME/logs
mkdir $PNAME/results
mkdir $PNAME/src
mkdir $PNAME/bin/slurm

echo "Creating files..."
touch $PNAME/README.md
echo "## ${BASENAME}" >> $RM
echo "# README.md" >> $RM
echo "# Author: Angus S. Hilts" >> $RM
echo "# Date: $(date +%d-%m-%Y)" >> $RM
echo "# Desc:" >> $RM
echo "A brief description of the project" >> $RM
echo "# Contents:" >> $RM
echo -e "bin \t-\tScripts and executable" >> $RM
echo -e "data \t-\tRaw data files (not included in git)" >> $RM
echo -e "doc \t-\tDocumentation and paper manuscripts" >> $RM

echo -e "logs \t-\tProgram and other log files, (not included in git)" >> $RM
echo -e "results -\tFinal results files only (included in git)" >> $RM
echo -e "src \t-\tSource code where necessary" >> $RM
echo "# Requirements" >> $RM

echo "Initialising git version control..."
git init $PNAME
echo "data/" >> $PNAME/.gitignore
echo "logs/" >> $PNAME/.gitignore
echo "**/tags" >> $PNAME/.gitignore

echo "Setting up Python..."
python3 -m venv $PNAME/env
source $PNAME/env/bin/activate

echo "Installing Jupyter notebook..."
pip3 install jupyter

echo "Creating notebook start script..."
echo "#!/usr/bin/env bash" >> $PNAME/bin/start_notebook.sh
echo "jupyter notebook --no-browser --port=8080" >> $PNAME/bin/start_notebook.sh
chmod +x $PNAME/bin/start_notebook.sh

echo "Done."
