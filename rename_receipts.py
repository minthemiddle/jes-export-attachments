import xml.etree.ElementTree as ET
from os import rename

tree = ET.parse('data.xml')
root = tree.getroot()

all_receipts = root[4]

for i in range(0,len(all_receipts)):
#for i in range(0,1):
    receipt_number = all_receipts[i][0].text
    receipt_attachment = all_receipts[i][4].attrib

    try:
        receipt_attachment_filename = receipt_attachment['filename']
        receipt_attachment_new_filename = receipt_number+'.jpg'
        rename(receipt_attachment_filename, receipt_attachment_new_filename)

    except KeyError:
        print('No attachment')