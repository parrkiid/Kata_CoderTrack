with open('./CordWithLyric.txt') as f:
    INPUT = f.read().splitlines()

for row in INPUT:
    row = row.replace('[C]', '[D]')
    row = row.replace('[Em]', '[F#m]')
    row = row.replace('[Dm]', '[Em]')
    row = row.replace('[G]', '[A]')
    row = row.replace('[F]', '[G]')
    row = row.replace('[Am]', '[Bm]')
    print(row)