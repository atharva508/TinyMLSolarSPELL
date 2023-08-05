# Tiny Machine Learning SolarSPELL

## [Google Drive](https://drive.google.com/drive/folders/1TZoLIc9k1t0jp1vpmh25c2iP8HFVnMFe)
.pdf files are not directly included in the drive but .txt files are included in a zip file in the drive called pdf_to_txt.zip

## Bard API
The API has a limited frequency (instead of a number cap) of requests that can be made to it, and it requires a __Secure-1PSID to be input as the Bard API key

### To get the __Secure-1PSID
   1. Open [Bard](https://bard.google.com)
   2. Open the console with F12
   3. Navigate to Application then Cookies
![](https://github.com/atharva508/TinyMLSolarSPELL/blob/main/bard_img.png)

For more details the Bard API is from https://github.com/dsdanielpark/Bard-API

# Code Documentation
The code will require you to have files in certain places.

Have a folder in your **own drive** called "ag" that has two folders: "content" and "pdf_to_txt"

Note: Only the "pdf_to_txt" folder is necessary for all code except the pdf_to_txt function in PDF_Reader.ipynb

The "content" folder will have all the .pdf files and the "pdf_to_txt" folder will have all the .txt files


## PDF_Reader.ipynb

### Extra files to manually add during runtime
* keywords_config.txt from the google drive (Download the keywords_config as a .txt file)

### Functions
* download_files_solarSPELL() - Downloads all files in parallel from http://solarspell-dev-web-server.dhcp.asu.edu/ag/content/
* pdf_to_txt(dir) - Converts .pdf files to .txt files
* setup_ag_data(dir) - 
