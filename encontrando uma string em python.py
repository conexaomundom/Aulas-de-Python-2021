def check_if_string_in_file(filename, string_to_search):
    #""" Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(filename, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                linha = line.split()
                
                return float(linha[-1])
    return ValueError('Esta conta não está cadastrada no banco')
