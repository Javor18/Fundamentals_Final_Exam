import re

count_of_barcodes = int(input())

for _ in range(count_of_barcodes):

    main_string = input()

    pattern = r'(\@\#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(\@\#+)'

    result = re.match(pattern, main_string)

    if not result:
        print("Invalid barcode")

    else:

        extract_numbers = re.findall('\d', result.group())

        if not extract_numbers:
            print('Product group: 00')

        else:
            print(f"Product group: {''.join(extract_numbers)}")