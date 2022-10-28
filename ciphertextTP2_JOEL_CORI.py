ciphertext = """iymyiiiwuhvruqwpimmwtiqqwdwduhtfomqtjxdsslkqhqpvurivvpsdemajiymosbgizchdwexgjcogtjaryawzmrryqeihkpqwtiqqwefxgppiqfchgizwhvdqvpcvurivvpsrfvesavaimiybtiuzzexgxiyibvbdsxuzqptraqhxevurtkmqrtzotxnjqjjdibticzvficuwqrivzfexeuqrijgextdzfltdmfvdzlsebvaolgfvugavbtibzaemdeaajqfczxnyczxtiamqjjideczvmwrzmzgtwqoxxfvdwtkburvnpugwtwzxpzveqpegembztmvxkqqwifbtipcqqruztyjgrvolxjmoickzmpecwfiavuqrijzmvtkpqqtkzamsfzseczaywpelfltjxmgtgqdeivailxtpfvnkwqbecwuxiymyiiiwuhhgwiigjbtigxiyiecikgddjurtjipztebgvtsieisfvqbecwdeizwzecuqfibxifltiqzklzbttarbrsgdmdecuzeldfbqvspvmqxtafltdmfvdzlsebvamvtwiysjjnaviymuvcfvxmcvidkpdmbpppetigvwzirrvdgddxxiivisebveuxwrnderkqardwbtixkmywpmiuppstqmckpqkpdmdxwvzqegvwhigrladteomqtjqzxwvaqvxvaflxjqzgallqwuzdqqpzvsebvayiiiwuhbvbdsxubisgimfygewrwpdcewjgmdqtkzamsdmfvdzlryhzwzecuuqxgfqphgvipxlfabmcfnrkpdmejdibtigeqzxtelahhwiymapuqxgfqptgzuqtxejmparvpqtkzamsgzuqtwmpigrbuscwwdgtrnuvhkxqvhfvdesmmzxjimsebveuxwnqdiavaeecuwzpxemyyakqbpppmdqtkzamsgzuqtyczxtiafltdmfvdzlbvxdmdxgztakndmfvdzlbvxdmyiiiwuheiqyiinwqgwfmeecuuqxgfqptgzuqxwimqgdizgtizwzecuzyiiiwuhdkpqvbraiiaciezpiqayhfbtiggwdxhrvpvtdiwih"""


# Taille maximale de la clé. Vous savez d'avance que la clé est d'une taille
# inférieure ou égale à 10 caractères.
maximum_key_size = 10

# Freq_dictfreq_dictuences de chaque caractere dans la langue anglaise
# (sur un total de 1. Ex : pour le "a", 0.0808 signifie donc 8.08 %)
english_freq_dict = [0.0808, 0.0167, 0.0318, 0.0399, 0.1256, 0.0217, 0.0180, \
                  0.0527, 0.0724, 0.0014, 0.0063, 0.0404, 0.0260, 0.0738, \
                  0.0747, 0.0191, 0.0009, 0.0642, 0.0659, 0.0915, 0.0279, \
                  0.0100, 0.0189, 0.0021, 0.0165, 0.0007]



#Etape 1 
def key_lenght():
    keys = {} # key = key lenght   value = score

    N = len(ciphertext)
    L = 1

    while L <= maximum_key_size:
        sumNL = 0 
        i=0
        for char_compared in ciphertext:
            if (i + L) < len(ciphertext):             
                if char_compared == ciphertext[i + L]:
                    sumNL+=1
            i+=1

        keys[L] = (sumNL/(N-L))
        L+=1

    K = max(keys, key=keys.get)  
    print("Key lenght " + str(K))
    return int(K)


def strip_text():
    K = key_lenght()
    text_strips = []

    for x in range(K):
        i = x
        strip = ""
        for y in range(len(ciphertext)-K):
            if i < len(ciphertext):
                strip+=ciphertext[i]
            i+=K
        text_strips.append(strip)
    print("Text strips:")
    print(text_strips)
    return text_strips


#Etape 2
def cesar():
    text_strips = strip_text()
    dec_dist_dict = {}
    key = []
    
    for text in text_strips:
        dec_dict = {} #chaque decalage de chaque sous texte a sa propre frequence sous forme de liste
        temp = -1
        dist_min = 10

        for dec in range(25):
            freq_dict = {} #dictionaire qui permet le calcul des frequence des lettres  
            for letter in text: #calcul frequence
                letter = (ord(letter) - 97 + dec) % 26
                if letter in freq_dict:
                    freq_dict[letter] += 1/len(text)
                else:
                    freq_dict[letter] = 1/len(text)
            
            dec_dict[dec] = freq_dict

        """Description des differents disctionaires:

            dec_dict ==> dec_dict[decalage] -> {freq_dict[position dans l'apha.] -> frequence}
                
            freq_dict ==> freq_dict[position dans l'aphabet] -> frequence 
           
            dec_dist_dict ==> dec_dist_dict[decalage en soit] -> valeur distance selon la formule de l'enonce """
        
        for k_dec, v_freq_dict in dec_dict.items():
            distdec = 0
            for k_pos,v_freq in v_freq_dict.items():
                distdec += pow((english_freq_dict[k_pos] - v_freq_dict[k_pos]),2)
            distdec = pow(distdec,(1/2))
            dec_dist_dict[k_dec] = distdec 
                 
        for k, v in dec_dist_dict.items():
            if v < dist_min:
                dist_min = v
                temp = k
        key.append(temp)
    print("Key indexes:")
    print(key)
    return key


#Etape 3

def decrypt():
    key_l = key_lenght()
    key_num = cesar()
    result = ""
    for x in range (len(ciphertext)):
        result += chr((((ord(ciphertext[x]) -97) + key_num[x % key_l]) % 26)+97)
    
    #Resultat final. Bisous Raph. ;)
    
    print("\n")
    print("Text decrypted:\n")
    print("============================================\n")
    print(result+ "\n")
    print("============================================\n")


if __name__ =="__main__":
    decrypt()



