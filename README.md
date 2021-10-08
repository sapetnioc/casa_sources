# casa_sources
Project to test new way of managing sources and build with a much smaller brainvisa-cmake.
```
wget https://brainvisa.info/download/casa-dev-5.0-4.sif
chmod +x casa-dev-5.0-4.sif
sudo pip3 install vcstool
git clone https://github.com/sapetnioc/casa_sources
cd casa_sources
vcs import < components.yaml
cd ..
mkdir build
cd build
../casa-dev-5.0-4.sif ../casa_sources/setup
build/bin/bv2 cmake ../casa_sources
build/bin/bv2 make -j10
```
