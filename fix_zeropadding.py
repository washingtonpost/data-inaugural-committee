import csv

lines = []
with open('inaugural_donations.csv','rU') as infile:
    reader = csv.DictReader(infile)
    fieldnames=reader.fieldnames
    with open('inaug_zero_fixed.csv','wU') as outfile:
        writer = csv.DictWriter(outfile,fieldnames=fieldnames)
        writer.writeheader()
        for line in reader:
            z = line['zip_code']
            z = z.zfill(5)
            line['zip_code'] = z
            writer.writerow(line)
