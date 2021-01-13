# Rapha Festive 500 - 2020
This is a project for tracking kilometers ridden on my bike during December 2020 for the Rapha Festive 500 on Strava in Python, using matplotlib, numpy, reportlab, and PySimpleGUI. 

## Motivation
The Rapha Festive 500 is a cycling challenge on the popular exercise tracking app Strava. The goal is to ride 500km from December 24-31. This project is based on the [Trek Century Challenge](https://github.com/dcribb19/trek_century_challenge) project that I did back in July.

Things that I needed to address:
1. Convert miles to kilometers
2. Throw in some festive colors
    - GUI
    - Graphs
3. Address the condensed timeframe (Dec 24-31 vs. entire month of July)

Extra: added some type hints


## Examples
<p align='center'>
    <img width=400 height=520 src=https://github.com/dcribb19/festive_500_2020/blob/main/examples/report_12_26.png> <img src=https://github.com/dcribb19/festive_500_2020/blob/main/examples/report_01_04.png width=400 height=520>
</p>

## Technologies
- Python 3.8
- matplotlib 3.3.3
- numpy 1.19.4
- PySimpleGUI 4.32.1
- reportlab 3.5.56

## Usage
```python
python ride_gui.py
```
1. GUI will display.  
<p align='center'>
    <img width=500 height=190 src=https://github.com/dcribb19/festive_500_2020/blob/main/examples/gui.png>
</p>

2. ... button will bring up calendar in order to select date.  
<p align='center'>
    <img width=500 height=262 src=https://github.com/dcribb19/festive_500_2020/blob/main/examples/gui_calendar.gif>
</p>  

3. Enter kilometers
4. Select location
5. Submit 
#### Output (All files saved with _month_day.extension)  
    - Bar chart saved as .jpg to graphs directory
    - Line graph saved as .jpg to graphs directory
    - Report .pdf saved to reports directory

## License
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)