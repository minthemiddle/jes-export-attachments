# Export attachments from JES

## Use Case

- [Jes](http://jes-eur.de) gives you the option to save attachments for receipts
- These attachments are stored in Jes' `.eux` file alongside the XML data for all receipts
- `.eux` files are basically `zip` files
- Sometimes you need a complete list of attachments, for example for your Finanzamt (tax office)
- This list must be ordered by receipt number


## What the script does and have

- The script parses the XML file for attachments and renames them to the receipt's number
- The script has an accompanying Jupyter file `rename_attachments.ipynb` which shows you step by step how the script works


## Requirements

- Python3
- Git
- Unzip tool

## How to use it (from your command line)

- Add receipts and attachments
- Save `.eux` file, e.g. `myreceipts.eux`
- Copy `myreceipts.eux` to `test.eux` as the file will not be useable after the renaming
- Rename `test.eux` to `test.zip`
- Unzip `test.zip`, which will give you a folder named `test`
- Enter folder `test`
- Clone Github repo: `git clone git@github.com:minthemiddle/jes-export-attachments.git`
- Run `python3 rename_receipts.py`
- Copy renamed images to a new folder
- Done


## Possible future development

- Automated unzipping
- Replace old filename with new one in XML and save integrity of file
- PDF stamp of receipt number on attachments as described [here](http://stackoverflow.com/questions/2925484/place-image-over-pdf)
