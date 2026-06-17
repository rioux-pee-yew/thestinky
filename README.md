Start with downloading pycharm and GIT.
Once that is done, add a local interpretor. You want to change the type to Conda and make sure that it is running python 3.12
You will need to download miniconda and it will have a fit. In the anaconda prompt thingy (its like command prompt) type in either

  conda config --set accept_tos yes
  
OR these commands one at a time. This just lets you set up your virtual environment. 

  conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
  
  conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
  
  conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2

Pycharm may say you need to "run the latest version of python" when you click new script. If this happens let it happen but make sure you switch back
next you want the files in your directory so you will input these commands one after another

  git clone --recursive https://github.com/ByteDance-Seed/depth-anything-3.git
  
  cd depth-anything-3

I am not too sure how to make this consistent so I just throw stuff at the wall. The next step is to download torch

  pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
  
  pip install torch torchvision   
  
  pip install xformers "torch>=2" torchvision
  
  pip install -r requirements.txt
  
  pip install -e .
  
NOTE: MAKE SURE THERE IS A SPACE AFTER THE E

  pip install addict
