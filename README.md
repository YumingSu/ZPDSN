# ZPDSN
This is a PyTorch implementation of the paper : ZPDSN: Spatio-Temporal Meteorological Forecasting with Topological Data Analysis (submitted to [Computers and Geosciences](https://www.sciencedirect.com/journal/computers-and-geosciences)) 
## Hardware and Software Requirements
This code was tested on a system with the following specifications:
- Memory (RAM): 32GB
- Disk storage: 1TB
- GPU: 1x NVIDIA GeForce GTX 3080

The model is implemented using Python3 with dependencies specified in requirements.txt.
- Pytorch>=1.4
- networkx==2.5.1
- numpy==1.19.4
- scikit-learn==0.23.2
- scipy==1.4.1
- dionysus==2.0.8,
- ripser==0.4.1
- persim==0.1.1
## Dataset
The observed meteorological data used in this study are available from (WeatherBench([https://www.sciencedirect.com/journal/computers-and-geosciences](https://github.com/pangeo-data/WeatherBench)https://github.com/pangeo-data/WeatherBench)).
