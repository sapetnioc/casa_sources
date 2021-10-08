# casa_sources
Project to test new way of managing sources and build with a much smaller brainvisa-cmake.
```
wget https://brainvisa.info/download/casa-dev-5.0-5.sif
chmod +x casa-dev-5.0-5.sif
git clone https://github.com/sapetnioc/casa_sources
./casa-dev-5.0-4.sif casa_sources/setup
cd casa_sources
./bin/bv2 cmake .
./bin/bv2 make -j10
```
