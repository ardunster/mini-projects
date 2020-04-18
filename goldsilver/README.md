#goldsilver

This folder contains scripts related to a project to track the prices of gold and silver over time and raise alerts when price relative to the 200 day moving average hit certain levels. It is an exercise in Python to extract data from, and write data to, xlsx files, and scrape data off the web, and if possible set up to be run on a daily basis to keep information relatively up to date. 

Because of terms of service agreements and similar considerations I have not included the xlsx files, or text files of data I have manually copied and pasted from the web for the purposes of running my code (these files are all in .gitignore). However, I have included links for the data to be retrieved by any interested end users. 

It is debatable whether the previous day's London Fix prices are the most useful measure for up-to-date gold and silver pricing, however, they are the most easily retrievable (available in text in the source code of the linked page) and consistent over time (data for spot prices for even the previous day can fluctuate depending on when the page is loaded), so I have chosen to use this data for this project. 