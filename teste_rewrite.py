from EditandoValor import change_string_in_file

def change(filename, dados, servico, valor):
    on_string = new_service = change_string_in_file(filename = filename, string_to_search = dados, servico = servico, valor = valor) 

    f = open(filename, 'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(on_string[0], on_string[1])

    f = open(filename, 'w')
    f.write(newdata)
    f.write('\n')
    f.close()
    
    
    return print(newdata)
