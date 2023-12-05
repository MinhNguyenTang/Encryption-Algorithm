#imports start
from random import randint
from hashlib import sha256
import ast
import hashlib
import sys
import os
import string
import random
import base64
import secrets
from cryptography.fernet import Fernet
import re
#imports end

class ECRY:
    def __init__(self):
        '''
        print('Welcome to the Encrypt/Decrypt String Tool\n')
        choice = -1

        while choice != 0:
            choice = int(input('1 - Encrypt String\n2 - Decrypt String\n\n'))
            while choice != 0 or choice != 1 or choice != 2:
                choice = int(input('ValueError\n1 - Encrypt String\n2 - Decrypt String\n0 - Quit\n\n'))
            
            if choice != 0:
                text = opfile()

            if choice == 1:
                enc = encryption(text)
            elif choice == 2:
                dec = decryption(enc[0], enc[1], (enc[2], enc[3], enc[4], enc[5], enc[6]))
        '''
        pass
    
    def opfile(self):
        pfile = 'msg.txt'
        with open(pfile, 'r', encoding='utf8') as file:
            text = file.read()
        return text

    def encryption(self, text):
        rnd = 0
        div = len(text)//5
        div_text = []
        tempcar = ''
        rdml = []
        encmsg = ''

        for carac in text:
            if rnd <= div:
                tempcar += carac
                rnd += 1
            else:
                rnd = 0
                div_text.append(tempcar)
                tempcar = ''
                tempcar += carac
                rnd += 1
        div_text.append(tempcar)
        tempcar = ''
        rnd = 0
        print('--------------------------')
        print(div_text)
        print('--------------------------')

        for i in range(5):
            rdm = randint(0, 4)
            while rdm in rdml:
                rdm = randint(0, 4)
            
            #if len(rdml) == 0:
            if rdm == 0:
                #enc1 = encrypt.alg1(div_text[rdm])
                #print(enc1)
                #dec = encrypt.alg1_decrypt(msg)
                #print(dec)
                rdml.append(0)
            if rdm == 1:
                enc2 = encrypt.alg2(div_text[rdm], 'file2.txt')
                print(enc2)
                dec = encrypt.alg2_decrypt(enc2)
                rdml.append(1)
            if rdm == 2:
                #enc3 = encrypt.alg3(div_text[rdm])
                #print(enc3)
                rdml.append(2)
            if rdm == 3:
                #enc4 = encrypt.alg4(div_text[rdm])
                #print(enc4[0])
                #vals = enc4[1]
                #dec = encrypt.alg4_decrypt(enc4[0], enc4[1], (enc4[2], enc4[3], enc4[4]))
                #print(dec)
                rdml.append(3)
            if rdm == 4:
                #enc5 = encrypt.alg5(div_text[rdm])
                #print(enc5)
                #dec = encrypt.alg5_decrypt(enc5)
                #print(dec)
                rdml.append(4)
        '''
        for j in range(5):
            if rdml[j] == 0:
                encmsg += enc1
            if rdml[j] == 1:
                encmsg += enc2
            if rdml[j] == 2:
                encmsg += enc3
            if rdml[j] == 3:
                encmsg += enc4
            if rdml[j] == 4:
                encmsg += enc5
        
        return (encmsg, rdml, enc1, enc2, enc3, enc4, enc5)
        '''
    
    def decryption(self, etext, rdml, allenc):
        decmsg = ''
        
        for i in rdml:
            '''
            if i == 0:
                dec1 = encrypt.alg1_decrypt(allenc[0])
                decmsg += dec1
            '''
            if i == 1:
                dec2 = encrypt.alg2_decrypt(allenc[1])
                decmsg += dec2
            '''
            if i == 2:
                dec3 = encrypt.alg3_decrypt(allenc[2])
                decmsg += dec3
            '''
            '''
            if i == 3:
                dec4 = encrypt.alg4_decrypt(allenc[3])
                decmsg += dec4
            '''
            '''
            if i == 4:
                dec5 = encrypt.alg5_decrypt(allenc[4])
                decmsg += dec5
            '''
        
        return decmsg

    
    def alg1(self, text):
        pky = 'infos.txt'
        pwh = 'fichier.txt'

        def rdky(pky):
            with open(pky, 'r', encoding='utf8') as file:
                ky = file.read()
            return ky

        def rdpwh(pwh):
            try:
                with open(pwh, 'r', encoding='utf8') as file:
                    sp = file.read()
                return sp
            except FileNotFoundError:
                return None

        def cvoi(text):
            replacements = {'a': '7', 'e': '5', 'i': '3', 'o': '1', 'u': '4', 'y': '8'}
        
            md = text
            for old_char, new_char in replacements.items():
                md = md.replace(old_char, new_char)
        
            return md

        def vincy(text, ky):
            indice_key = 0
            msg_code = ""
        
            for i in range(0, len(text)):
                if 'A' <= text[i] <= 'Z' or 'a' <= text[i] <= 'z':
                    char_offset = ord('A') if 'A' <= text[i] <= 'Z' else ord('a')
                    msg_code += chr(((ord(text[i]) - char_offset + (ord(ky[indice_key]) - ord('A'))) % 26) + char_offset)
                    indice_key = (indice_key + 1) % len(ky)
                else:
                    msg_code += text[i]
            return msg_code

        def add_num(text):
            prefix = str(random.randint(1, 100))
            suffix = str(random.randint(1, 100))
            result = prefix + text + suffix
            return result

        def r(text):
            reversed_text = text[::-1]
            return reversed_text

        def wrfi(text, md):
            with open(text, 'w', encoding='utf8') as file:
                file.write(md)


        def ii(text):
            iiv = [ord(character) for character in text]
            return iiv

        s = text
        ky = rdky(pky)
        sp = rdpwh(pwh)

        if sp is None:
            uinp = input('')
            
            sp = hashlib.sha256(uinp.encode('utf-8')).hexdigest()
            with open(pwh, 'w', encoding='utf8') as file:
                file.write(sp)

        uinp = input('')

        if hashlib.sha256(uinp.encode('utf-8')).hexdigest() == sp:
            md = cvoi(s)
            md = vincy(md, ky)
            md = r(md)
            iiv = ii(md)
            iist = str(iiv)
            print('Ok')
        else:
            print('Error.')
        
        res = iist

        return res

    def alg1_decrypt(self, text):
        pky = 'infos.txt'
        pwh = 'fichier.txt'

        def read_key(pky):
            with open(pky, 'r', encoding='utf8') as file:
                ky = file.read()
            return ky

        def read_stored_password(pwh):
            try:
                with open(pwh, 'r', encoding='utf8') as file:
                    shp = file.read()
                return shp
            except FileNotFoundError:
                return None

        def authenticate_user(pwh):
            shp = read_stored_password(pwh)

            if shp is None:
                print('Fichier déchiffré')
                exit()

            uinp = input('')

            if hashlib.sha256(uinp.encode('utf-8')).hexdigest() != shp:
                print('Fichier déchiffré')
                exit()

        def cii(ascii_str):
            ascii_values = [ord(char) for char in ascii_str]
            ascii_str = ' '.join(map(str, ascii_values))
            return ascii_str



        def rt(t):
            rt = t[::-1]
            return rt

        def rvoi(t):
            replacements = {'7': 'a', '5': 'e', '3': 'i', '1': 'o', '4': 'u', '8': 'y'}
        
            rtx = t
            for old_char, new_char in replacements.items():
                rtx = rtx.replace(old_char, new_char)
        
            return rtx

        def rvincy(t, ky):
            iky = 0
            m = ""
        
            for i in range(0, len(t)):
                if 'A' <= t[i] <= 'Z' or 'a' <= t[i] <= 'z':
                    char_offset = ord('A') if 'A' <= t[i] <= 'Z' else ord('a')
                    m += chr(((ord(t[i]) - char_offset - (ord(ky[iky]) - ord('A'))) % 26) + char_offset)
                    iky = (iky + 1) % len(ky)
                else:
                    m += t[i]
            return m

        def wrfi(text, rtx):
            full_path = 'file.txt'
            with open(full_path, 'w', encoding='utf8') as file:
                file.write(text)

        authenticate_user(pwh)

        s = text
        ky = read_key(pky)
        t = cii(s)
        t = rt(t)
        t = rvincy(t, ky)
        rtx = rvoi(t)
        wrfi(text, rtx)
        print('Fichier déchiffré')

        def rtext(text):
            full_path = 'file.txt'
            with open(full_path, 'r', encoding='utf8') as file:
                tx = file.read()
            return tx
        
        res = rtext(text)

        return res
    
    def alg2(self, input='msg.txt', output='file2.txt'):

        def generate_the_key():
            key_length = 32
            key = secrets.token_bytes(key_length)

            return key
        
        def save_the_key(key, file="filekey.txt"):
            key_encoded = base64.b64encode(key).decode('utf-8')

            with open(file, 'w') as filekey:
                filekey.write(key_encoded)

            return key_encoded

        def encrypt_file(file_path, output_file_path):
            key = generate_the_key()
            save_the_key(key)

            fernet = Fernet(base64.b64encode(key).decode('utf-8'))

            with open(file_path, 'rb') as encrypted_file:
                original = encrypted_file.read()

            encrypted = fernet.encrypt(original)

            with open(output_file_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

            return encrypted

        return encrypt_file(input, output)
        
        
    def alg2_decrypt(self, input='file2.txt', output='msg_output.txt'):

        def upload_the_key(file="filekey.txt"):
            with open(file, 'r') as filekey:
                key_encoded = filekey.read()

            key = base64.b64decode(key_encoded)

            return key

        def decrypt_file(file_path, output_file_path):
            key = upload_the_key()
            fernet = Fernet(base64.b64encode(key).decode('utf-8'))

            with open(file_path, 'rb') as enc_file:
                encrypted = enc_file.read()

            decrypted = fernet.decrypt(encrypted)

            with open(output_file_path, 'wb') as dec_file:
                dec_file.write(decrypted)

            return decrypted

        return decrypt_file(input, output)

    def alg3(self, text):
        pass

    def alg3_decrypt(self, text):
        pass

    def alg4(self, text):
        rnd = 0
        div_text = []
        key = '' #MINIMUM 5 caractères
        k = []
        nwkey = ''
        wkey = ''
        knwwkey = ''
        nmbs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        mshanmb = ''
        mshacar = ''
        nmb = 0
        lsp = []
        opl = []
        cars = ['a', 'b', 'c', 'd', 'e', 'f']
        allcars = []
        cnt = 0
        cars_cnt = []
        lnwbtext = ''
        
        rnd = 48
        while rnd <= 57:
            allcars.append(chr(rnd))
            rnd += 1
        rnd = 65
        while rnd <= 90:
            allcars.append(chr(rnd))
            rnd += 1
        rnd = 97
        while rnd <= 122:
            allcars.append(chr(rnd))
            rnd += 1
        rnd = 0

        if len(key) == 0:
            rdm = randint(5, 60)
            while len(key) < rdm:
                rdmcars = randint(0, len(allcars)-1)
                key += allcars[rdmcars]
            rdm = 0
        print('key:')
        print(key)
        print('**********')

        tempcar = ''
        for elem in text:
            if elem != ' ':
                tempcar += elem
            else:
                lsp.append(rnd)
            rnd += 1
        wstext = tempcar
        tempcar = ''
        rnd = 0

        if len(wstext) > 16:
            div = 2
            while len(wstext)//div > 16:
                div += 1
            
            tempcar = ''
            for carac in wstext:
                if rnd <= div:
                    tempcar += carac
                    rnd += 1
                else:
                    rnd = 0
                    div_text.append(tempcar)
                    tempcar = ''
                    tempcar += carac
                    rnd += 1
            div_text.append(tempcar)
            tempcar = ''
            rnd = 0
        else:
            div_text.append(wstext)
        
        while len(div_text[-1]) != len(div_text[0]):
            div_text[-1] += div_text[-1][rnd]
            rnd += 1
        rnd = 0
        
        for i in range(len(key)//3):
            rdm = randint(0, len(key)-1)
            k.append(key[rdm])
        
        for j in key:
            rnd += 1
            if j not in k:
                nwkey += j
        rnd = 0

        mid = (len(nwkey)//2)-1
        if len(nwkey) >= 1 and len(nwkey) <= 2:
            for k in range(3):
                wkey += nwkey[0]
        elif len(nwkey) > 2 and len(nwkey) < 5:
            wkey += nwkey[mid-1]
            wkey += nwkey[mid]
            wkey += nwkey[mid+1]
        else:
            wkey += nwkey[mid-2]
            wkey += nwkey[mid]
            wkey += nwkey[mid+2]
        
        ksha = sha256(key.encode('utf-8')).hexdigest()
        nwsha = sha256(nwkey.encode('utf-8')).hexdigest()
        wsha = sha256(wkey.encode('utf-8')).hexdigest()

        lenshakey = (len(ksha) + len(nwsha) + len(wsha))

        for l in range(lenshakey//3):
            knwwkey += ksha[l]
            knwwkey += nwsha[l]
            knwwkey += wsha[l]

        for m in knwwkey:
            if m not in nmbs:
                mshacar += m
            else:
                mshanmb += m

        while rnd < len(mshanmb)-1:
            op = randint(0, 1)
            if op == 0:
                nmb -= int(mshanmb[rnd])
                opl.append('-')
            else:
                nmb += int(mshanmb[rnd])
                opl.append('+')
            rnd += 1
        rnd = 0

        for i in range(6):
            rnd = 0
            for n in mshacar:
                if n == cars[rnd]:
                    cnt += 1
            rnd += 1
            cars_cnt.append(cnt)
            cnt = 0
        rnd = 0
        cars_cnt.insert(3, nmb)
        cars_cnt.insert(0, nmb//cars_cnt[0])
        cars_cnt.append(nmb*cars_cnt[0])

        for ptext in div_text:
            btext = int(ptext, 32)

            
            print('---------------------------------------------')
            print(btext)
            print('---------------------------------------------')


            if cars_cnt[0] == 0 and nmb == 0:
                btext = (btext - cars_cnt[-1])
            elif cars_cnt[0] == 0:
                btext = ((btext - cars_cnt[-1])//nmb)
            elif nmb == 0:
                btext = (btext - cars_cnt[-1])*cars_cnt[0]
            else:
                btext = ((btext - cars_cnt[-1])//nmb)*cars_cnt[0]
            
            print(str(btext) + '(-)')
            print('---------------------------------------------')

            btext = str(btext)
            
            while len(btext) < 10:
                btext += btext[rnd]
                rnd += 1
            rnd = 0
            
            if len(btext) > 10:
                bttext = btext
                btext = ''
                while len(btext) < 10:
                    btext += bttext[rnd]
                    rnd += 1
                rnd = 0
            
            b6text = btext[4:6]
            b2text = btext[0:2]
            b3text = btext[2:4]
            b4text = btext[6:8]
            b5text = btext[8:10]

            btext = int(btext)
            b2text = int(b2text)
            b3text = int(b3text)
            b4text = int(b4text)
            b5text = int(b5text)
            b6text = int(b6text)
            b2text = (b2text+5)*4
            b3text = (b3text+7)*2
            b4text = (b4text+14)*3
            b5text = (b5text+1)*2
            nwbtext = chr(b5text)
            nwbtext += chr(b4text)
            nwbtext += chr(b6text)
            nwbtext += chr(b3text)
            nwbtext += chr(b2text)
            b2text = str(b2text)
            b3text = str(b3text)
            b4text = str(b4text)
            b5text = str(b5text)
            b6text = str(b6text)
            
            lnwbtext += nwbtext
        
        return (lnwbtext, knwwkey, k, opl, cars_cnt)
    
    def alg4_decrypt(self, etext, key, vals):
        def keypass(key, k):
            keylog = input('')
            
            rnd = 0
            nwkey = ''
            wkey = ''
            knwwkey = ''
            
            for j in keylog:
                rnd += 1
                if j not in k:
                    nwkey += j
            rnd = 0

            mid = (len(nwkey)//2)-1
            if len(nwkey) >= 1 and len(nwkey) <= 2:
                for k in range(3):
                    wkey += nwkey[0]
            elif len(nwkey) > 2 and len(nwkey) < 5:
                wkey += nwkey[mid-1]
                wkey += nwkey[mid]
                wkey += nwkey[mid+1]
            else:
                wkey += nwkey[mid-2]
                wkey += nwkey[mid]
                wkey += nwkey[mid+2]
            
            ksha = sha256(keylog.encode('utf-8')).hexdigest()
            nwsha = sha256(nwkey.encode('utf-8')).hexdigest()
            wsha = sha256(wkey.encode('utf-8')).hexdigest()

            lenshakey = (len(ksha) + len(nwsha) + len(wsha))

            for l in range(lenshakey//3):
                knwwkey += ksha[l]
                knwwkey += nwsha[l]
                knwwkey += wsha[l]
            

            if knwwkey == key:
                print(True)
                return True
            else:
                print(False)
                return False
        
        keyres = keypass(key, vals[0])
        while keyres == False:
            keyres = keypass(key, vals[0])
        
        def base32_to_str(btstext):
            decoded_bytes = base64.b32decode(btstext)
            result_str = decoded_bytes.decode('utf-8')
            
            return result_str
        

        rnd = 0
        petext = len(etext)//(len(etext)//5)
        nwbtext = ''
        bltext = []

        while rnd < len(etext):
            for i in range(petext):
                nwbtext += etext[rnd]
                rnd += 1
            bltext.append(nwbtext)
            nwbtext = ''
        rnd = 0

        for ptext in bltext:
            btext = ''

            b5text = ptext[0]
            b4text = ptext[1]
            b6text = ptext[2]
            b3text = ptext[3]
            b2text = ptext[4]

            b5text = ord(b5text)
            b4text = ord(b4text)
            b6text = ord(b6text)
            b3text = ord(b3text)
            b2text = ord(b2text)

            b2text = (b2text//4)-5
            b3text = (b3text//2)-7
            b4text = (b4text//3)-14
            b5text = (b5text//2)-1

            b2text = str(b2text)
            b3text = str(b3text)
            b4text = str(b4text)
            b5text = str(b5text)
            b6text = str(b6text)
            
            while len(b2text) != 2:
                b2text = '0' + b2text
            while len(b3text) != 2:
                b3text = '0' + b3text
            while len(b6text) != 2:
                b6text = '0' + b6text
            while len(b4text) != 2:
                b4text = '0' + b4text
            while len(b5text) != 2:
                b5text = '0' + b5text

            btext += b2text
            btext += b3text
            btext += b6text
            btext += b4text
            btext += b5text

            while len(btext) == 10:
                if rnd != 0 and rnd != 1 and rnd != 2 and btext[0:rnd] == btext[rnd:rnd*2]:
                    btext = btext[0:rnd]
                rnd += 1
            rnd = 0

            btext = int(btext)

            print('///////////////////')
            print(str(btext) + '(-)')
            print('///////////////////')

            if vals[2][0] == 0 and vals[2][4] == 0:
                btext = (btext + vals[2][-1])
            elif vals[2][0] == 0:
                btext = ((btext + vals[2][-1]) * vals[2][4])
            elif vals[2][4] == 0:
                btext = (btext + vals[2][-1]) // vals[2][0]
            else:
                btext = ((btext + vals[2][-1]) * vals[2][4]) // vals[2][0]
            
            btext = str(btext)
            
            print(btext)
            print('///////////////////')
            
            '''
            btstext = btext
            itext = base32_to_str(btstext)
            print(itext)
            '''
    def alg5(self, text):
        print(text)
        caracteres_speciaux = ['أ', 'Б', 'シ', 'د', 'イ', 'ف', 'ج', 'ハ', 'И', 'ジ', 'ك', 'Л', 'م', 'Н', 'オ', 'П', 'ق', 'Р', 'セ', 'ت', 'У', 'В', 'و', 'クス', 'У', 'ز']

        def substituer_lettre(lettre):
            if lettre.isalpha():
                return random.choice(caracteres_speciaux)
            else:
                return lettre

        def chiffrement_substitution(message):
            message_chiffre = ""
            for caractere in message:
                message_chiffre += substituer_lettre(caractere)

            return message_chiffre

        def chiffrement_substitution_fichier(text):
            contenu_chiffre = chiffrement_substitution(text)

            contenu_mele = decoupage_et_melange(contenu_chiffre)

            return contenu_mele

        def decoupage_et_melange(texte_chiffre):
            morceaux = re.findall(r'\b\w+\b', texte_chiffre)

            random.shuffle(morceaux)

            texte_mele = ' '.join(morceaux)

            return texte_mele
 
        return chiffrement_substitution_fichier(text)

    def alg5_decrypt(self, text):
        caracteres_speciaux = ['أ', 'Б', 'シ', 'د', 'イ', 'ف', 'ج', 'ハ', 'И', 'ジ', 'ك', 'Л', 'م', 'Н', 'オ', 'П', 'ق', 'Р', 'セ', 'ت', 'У', 'В', 'و', 'Ку', 'У', 'з']

        # Fonction pour substituer une lettre par un caractère spécial aléatoire
        def substituer_lettre(lettre):
            if lettre.isalpha():
                return random.choice(caracteres_speciaux)
            else:
                return lettre

        # Fonction pour déchiffrer un caractère spécial vers la lettre d'origine
        def dechiffrer_caractere(caractere_chiffre):
            correspondances = {'أ': 'A', 'Б': 'B', 'シ': 'S', 'د': 'D', 'イ': 'I', 'ف': 'F', 'ج': 'J', 'ハ': 'H', 'И': 'N',
                            'ジ': 'J', 'ك': 'K', 'Л': 'L', 'م': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'ق': 'Q', 'Р': 'R',
                            'セ': 'S', 'ت': 'T', 'У': 'U', 'В': 'V', 'و': 'W', 'Ку': 'Ku', 'У': 'U', 'з': 'Z'}

            if caractere_chiffre in correspondances:
                return correspondances[caractere_chiffre]
            else:
                return caractere_chiffre

        # Fonction de déchiffrement
        def dechiffrement_substitution(message_chiffre):
            message_dechiffre = ""
            for caractere_chiffre in message_chiffre:
                message_dechiffre += dechiffrer_caractere(caractere_chiffre)

            return message_dechiffre

        # Exemple d'utilisation avec un fichier texte.txt
        def dechiffrement_substitution_fichier(contenu_chiffre):
            print(f"Texte chiffré :\n{contenu_chiffre}\n")

            contenu_dechiffre = dechiffrement_substitution(contenu_chiffre)

            print(f"Résultat du déchiffrement:\n{contenu_dechiffre}")

            return contenu_dechiffre
        
        message_dechiffre = dechiffrement_substitution_fichier(text)

        return message_dechiffre



encrypt = ECRY()
text = encrypt.opfile()
encrypt.encryption(text)