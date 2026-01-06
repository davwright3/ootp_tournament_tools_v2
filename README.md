# AU OOTP Tournament Tools v2

## Welcome to the new version of the OOTP Tournament Utility

This version builds on the lessons learned from the original utility tool
which can be found here: [GithubLink](https://github.com/davwright3/au_ootp_tournament_utilities)

Please visit this link if you have any feature requests: [Feature Requests](https://docs.google.com/forms/d/1I01oUCsnH41OVFDkNjZeQurVAMr5zBd8103BPOorBUw/edit)

## Current Version 0.6.0

### Updated: 

6 Jan 2026

Final release for OOTP Perfect Team 26 Edition

- Adds batting and pitching ranking slideshows

  - Batters currently ranked on a custom formula using wOBA and baserunning/fielding ratings
  - Pitchers ranked on strikeout percentage minus walk and home run percentage formula

- Adds ability to customize basic views going back for a set number of days

- Added framework for data visualization

  - Includes custom frames and matplotlib methods for plotting using single and double inputs
  - Data visualization is planned to be added with first update to OOTP Perfect Team 27 in late March/early April


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

- Create your view on the OOTP Sortable Stats page and export the file (with both batters and pitchers) to CSV

  - View should include the following stats, in this order:
  
    - Tag Controls, PT Card ID, Organization, PT Card Value, PT Is Variant, PT Variant Level, (Batter) G, GS, PA, AB, H, 1B, 2B, 3B, HR, RBI, R, BB, IBB,
      HP, SH, SF, SO, GIDP, EBH, TB, RC, RC/27, wOBA, WPA, WAR, SB, CS, wSB, UBR, BsR, (Pitcher) G, GS, W, L, SVO, SV, BS, HLD, SD, MD, IP, BF, AB, HA, 1B,
      2B, 3B, HR, TB, R, ER, BB, IBB, K, HP, SH, SF, WP, DP, IR, IRS, QS, CG, SHO, GB, FB, SB, CS, FIP, WAR, TC, A, PO, E, DP, TP, PCT, ZR, SBA, RTO

  - Once exported, copy the file into your desired raw data folder, and name according the the file naming conventions below

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

## File Naming Conventions

- When files are processed, the app uses the names of the files to determine if they have already been added to the 'ready' CSV
- When loading, the app will parse these filenames to the best of its ability in order to be able to process data
- <span style='color:red'>For best results:</span>

  - For daily and weekly tournaments, use a DD Mmm format (i.e. 03 Sep)
  - For quick tournaments use a four digit integer number referencing the tournament (i.e. 0345)

- Adding extraneous letters or numbers may cause errors in data processing

## Processing Files

- A template file, with headings that match the required view, is provided for the file processing app

  - After clicking the create a new file button, you will be asked to enter a name for the file
  - A new empty file with proper headings will be copied to the location in your settings for your Ready File Location
  - This location can be viewed on the home page of the app, if you have trouble finding the file after creation

- Processing steps:

  - Select target file: this is the file you want the raw data to be concatenated to
  - Select raw data folder: this is the folder where your raw data is stored.  

    - It is normal to not see any files when selecting, as this step is looking for a folder

  - Process files

    - The app uses the filename to enter into the 'Trny' column in the concatenated file
    - This allows the app to avoid copying duplicate files into the new folder
    - You will see the names of the processed files and how many lines are added in the window messaging system

## Viewing Statistics

- Upon opening the Basic Stats section of the app, you will need to use the file select button to select the tournament data you wish to view

  - Until a valid CSV file is selected, the batting and pitching stats view buttons will be inactive (unclickable)

- Upon opening the stats view, all possible stats to view will be selected, and will default to baseline filter (i.e. minimum of 600 plate appearances)
- You will then be able to make your options and filter selections and press the reload button to view only the options that you want


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
  concerns that are outside of the scope of this project.

- <span style="font-weight:bold">Why are my tables empty?</span>

  - There are a few reasons your table may populate as empty, plase check the following:

    - Ensure that the headings you exported from OOTP are accurate, and that the dataset contains both batters and pitchers

      - If batters and pitchers are exported in separate datasets, the cull teams functions will not work and all of your players will be removed from the data set

    - Check your filenames for the proper format (DD MMM or XXXX depending on tournament type)
    - Check your minimum settings for plate appearances or innings pitched

### Previous Versions

02 Oct 2025 v0.2.0

New Features:

- File Processing System 🗃️

  - Uses Pandas Dataframes to quickly append raw CSV files into a single file for stat calculations
  - Improved responsiveness and error protection/detection
  - Updated UI/UX to provide better readability and usability for users

- Simpler settings updates 🛠️

  - Settings updates are handled by the individual setting instead of in a setting menu
  - Better UI indications on valid/invalid file paths and file selections
  - Improved checks for invalid files, allowing for reduced errors from stat calculations and missing data

- Improved main view display options

  - Ability to control Joe Unknown cutoff limits
  - View only cards in your collection
  - More robust stats selections (i.e. K-BB pct, Last 10 pricing, etc.)

- New User Messaging System 💬

  - New logs on various pages provide improved communication to the user
  - Provides instant feedback to the user, without having to override other data labels
  - Color coded by message tag

22 Oct 2025

New Features:

- Team Statistics App 🔢

  - Display team wins, losses, winning percentages
  - Select minimum number of games played (default: 20)
  - All stats that are in the batter and pitcher stats are available to view

- Ratings Comparison Tool ➕➖

  - View batting, pitching, defense, baserunning ratings and compare across players
  - View overall ratings, by side, and splits
  - Select year and value ranges, as well as card types
  - Select weight for each rating (user determined, default: 1x)

14 Nov 2025

New Features:

- Player Cards are Live

  - Cards contain player ratings, player stats for all teams, player stats for selected team, and league stats
  - In order to facilitate the player stats for the selected team, a team selection dropdown has been added to the basic stats app home page

- New Team Cards available

  - Double-clicking on a team in the team stats app will open a new card with the players who have appeared for that team
  - Player cards are also clickable from this page and will open in a new window

- A few new stats added to the player stats that are available

- Updated resource path checking, which should fix pathing issue for the logos and new files on MACos.  (Please inform me if this is not the case, as I cannot test on Mac.)

- For developers:

  - Linting is complete for all base scripts using Flake8 and updated to PEP 8.  This should make it easier for developers to make their updates from the source code.
