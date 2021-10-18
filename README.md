# 3dPlotGenerator

This program takes the output of a packet analyzer, and generates a PER (Packet Error Rate) report. 
The script extracts data from the output text file selected by the user. <br />
The report consists of 5 plots, one for each tested tx power level. Plots are generated using Matplotlib. <br />
It is able to calculate the percentage of the sent packets that were received successfully. This is displayed above each plot.

Example: <br />
![screenshot](https://github.com/jibeombae/3dPlotGenerator/blob/master/test_example.jpg)
