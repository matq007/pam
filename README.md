### PAM

PAM is a Personal Appliance Manager for your house or flat. It can integrate with all smart devices. 
You can control PAM with your voice. 

### Installation

```
sudo apt-get install python-pip
sudo pip install requirements.txt
```

### Change voice

```
sudo apt-get install festlex-cmu

cd /usr/share/festival/voices/english/
sudo wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
sudo tar jxf cmu_us_clb_arctic-0.95-release.tar.bz2 
sudo ln -s cmu_us_clb_arctic cmu_us_clb_arctic_clunits
sudo cp /etc/festival.scm /etc/festival.scm.backup
sudo echo "(set! voice_default 'voice_cmu_us_clb_arctic_clunits)" >> /etc/festival.scm
```

### Authors

 * Martin Proks <<mproksik@gmail.com>>
 * Simon Bozhilov <<simonbozhilov@gmail.com>>
 * Iustinian Olaru  <<o.iustin@gmail.com>>