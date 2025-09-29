# AU OOTP Tournament Tools v2

## Welcome to the new version of the OOTP Tournament Utility

This version builds on the lessons learned from the original utility tool
which can be found here: [GithubLink](https://github.com/davwright3/au_ootp_tournament_utilities)

Please visit this link if you have any feature requests: [Feature Requests](https://docs.google.com/forms/d/1I01oUCsnH41OVFDkNjZeQurVAMr5zBd8103BPOorBUw/edit)

## Current Version 0.1.2

### Updated: 

11 Sep 2025

New Features:

- File Processing System 🗃️

  - Uses Pandas Dataframes to quickly append raw CSV files into a single file for stat calculations
  - Improved responsiveness and error protection/detection
  - Updated UI/UX to provide better readability and usability for users

- Simpler settings updates 🛠️

  - Settings updates are handled by the individual setting instead of in a setting menu
  - Better UI indications on valid/invalid file paths and file selections
  - Improved checks for invalid files, allowing for reduced errors from stat calculations and missing data

- New User Messaging System 💬

  - New logs on various pages provide improved communication to the user
  - Provides instant feedback to the user, without having to override other data labels
  - Color coded by message tag

## Installation

- Windows 🪟:
  
  - Under the "Releases" menu and the most recent release, select the 'windows-x64.exe' file and it will download automatically.
  - Upon opening the file, you may get a screen that says Defender stopped an unrecognized app from opening.

    - Click on 'More Info' and then 'Run Anyway'.

  - Select the folder you wish to install to and whether you want a desktop icon to be created.

- macOS 🍎:

  - Under the "Releases" menu, on the most recent release, select the 'macos-universal.zip'.
  - Once downloaded, double click, and it should open automatically.


## Initial Use

- When first opening the program you will be required to set up your file paths for select items:

  - These settings are selected from the file selection buttons at the bottom of the home page.
  - <span style="color:orange">(MANDATORY) You must select the path for your OOTP Perfect Team Card Dump.</span>
  
    - By default, this file is created when you click the "Export Card List" button on the shop, and is located in your 'OOTP Baseball XX/online_data' folder

  - <span style="color:violet">(HIGHLY RECOMMENDED)</span> Set your 'Tgt Data' folder to the location where you want your processed data files to exist.  

    - This is where the template file will be copied to when you create a new file to process to.  Without updating this setting, it will default to 'C:/'

  - <span style="color:green">(RECOMMENDED)</span> Set your 'Raw Data' folder to the root of where you will be storing your CSV's that you download from OOTP Perfect Team.

    - This folder will be where the initial file dialog opens when you prepare to process files.


## Recommended file structure:

- For the best workflow, I recommend the following file structure for your downloaded and processed data:

  Root

  |-- Raw Data

  ||-- Tournament Name

  |||-- Month

  ||||-- DD MMM.csv OR xxxx.csv where xxxx is the integer number of the quick tournaments

  |-- Ready Data

  ||-- tournament_name.csv

  ||-- tournament_2_name.csv


## Project Roadmap

<span style="color:violet">ALL DATES ARE TENTATIVE</span>

- <span style="color:red">3 October</span>: Initial Public Beta Release (v0.2.0)

  - File Processing
  - Basic Batting and Pitching Stats

    - Tools for selecting which stats to see, min/max player ratings and plate appearances, batting side, position, etc.

- <span style="color:red">17 October</span>: Basic Team Stats and Ratings Comparison Tool (v0.3.0)

  - Team win/loss and statistics totals with team selection and highlighting
  - Comparison tool for cards with user selected weighting 
  
- <span style="color:red">31 October</span>: Player Cards (v0.3.0)

  - Player trends over time, overall stats, and stats by selected team
  - Player ratings viewer and other information

- <span style="color:red">Future</span>: 

  - Tournament wide stats trends over time
  - Single screen player comparison over time
  - (Low Priority) Player modeling using scikit-learn or other ML scripting

## FAQ's

- <span style="font-weight:bold">Can I contribute to the data?</span>

  - At the moment I have no plans to utilize a community dataset.  While I appreciate the thought, 
  the program is designed for personal use, and allowing external sources to input data would introduce security 
  concerns that are outside of the 
