import pandas as pd

# OCR results (simplified for this example)
ocr_results = [
    ([[260, 684], [368, 684], [368, 710], [260, 710]], 'Sub Total:', 0.9201565369805678),
    ([[650, 680], [714, 680], [714, 706], [650, 706]], 'E8.00', 0.9719274551369801),
    ([[257, 863], [351, 863], [351, 899], [257, 899]], 'Total:', 0.9986760608727725),
    ([[627, 857], [719, 857], [719, 895], [627, 895]], 'E4.50', 0.875225866526062)
]

# Extract "Sub Total" and "Total" values
sub_total = None
total = None

for result in ocr_results:
    text = result[1]
    if 'Sub Total' in text:
        sub_total = ocr_results[ocr_results.index(result) + 1][1]
    elif 'Total' in text:
        total = ocr_results[ocr_results.index(result) + 1][1]

# Create a DataFrame
data = {'Sub Total': [sub_total], 'Total': [total]}
df = pd.DataFrame(data)
df