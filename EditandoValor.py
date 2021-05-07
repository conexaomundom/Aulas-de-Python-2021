def change_string_in_file(filename, string_to_search, servico, valor):
    #""" Check if any line in the file contains given string """
    # Open the file in read only mode
    with open(filename, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                old_string = line
                linha = line.split()
                old_saldo = float(linha[-1])
                if servico == 'deposito':
                    novo_saldo = old_saldo + valor
                elif servico == 'saque':
                    if valor > old_saldo:
                        raise ValueError('Valor a ser sacado excede o saldo atual')
                    novo_saldo = old_saldo - valor
                    
                linha[-1] = str(novo_saldo)
                new_string = ' '.join(linha) + ' \n'
                #new_string = new_string + ' \n'


                f = open(filename, 'r')
                filedata = f.read()
                f.close()

                newdata = filedata.replace(old_string, new_string)

                f = open(filename, 'w')
                f.write(newdata)
                f.close()
                
                return  print(newdata)
    return ValueError('Esta conta não está cadastrada no banco')
    
    
