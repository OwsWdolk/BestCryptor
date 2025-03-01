import random, time, os
from colorama import *
init(autoreset=True)

a = """
 █     █░▓█████▄  ▒█████   ██▓     ██ ▄█▀
▓█░ █ ░█░▒██▀ ██▌▒██▒  ██▒▓██▒     ██▄█▒ 
▒█░ █ ░█ ░██   █▌▒██░  ██▒▒██░    ▓███▄░ 
░█░ █ ░█ ░▓█▄   ▌▒██   ██░▒██░    ▓██ █▄ 
░░██▒██▓ ░▒████▓ ░ ████▓▒░░██████▒▒██▒ █▄
░ ▓░▒ ▒   ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▒ ▓▒
  ▒ ░ ░   ░ ▒  ▒   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒ ▒░
  ░   ░   ░ ░  ░ ░ ░ ░ ▒    ░ ░   ░ ░░ ░ 
    ░       ░        ░ ░      ░  ░░  ░   
          ░
"""
b = """
░  ░░░░  ░░       ░░░░      ░░░  ░░░░░░░░  ░░░░  ░
▒  ▒  ▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒  ▒▒
▓        ▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓
█   ██   ██  ████  ██  ████  ██  ████████  ███  ██
█  ████  ██       ████      ███        ██  ████  █
"""
c = """
██╗    ██╗██████╗  ██████╗ ██╗     ██╗  ██╗
██║    ██║██╔══██╗██╔═══██╗██║     ██║ ██╔╝
██║ █╗ ██║██║  ██║██║   ██║██║     █████╔╝ 
██║███╗██║██║  ██║██║   ██║██║     ██╔═██╗ 
╚███╔███╔╝██████╔╝╚██████╔╝███████╗██║  ██╗
 ╚══╝╚══╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
d = """
 .S     S.    .S_sSSs      sSSs_sSSs    S.       .S    S.   
.SS     SS.  .SS~YS##b    d##SP~YS##b   SS.     .SS    SS.  
S%S     S%S  S%S   `S#b  d%S'     `S#b  S%S     S%S    S&S  
S%S     S%S  S%S    S%S  S%S       S%S  S%S     S%S    d*S  
S%S     S%S  S%S    S&S  S&S       S&S  S&S     S&S   .S*S  
S&S     S&S  S&S    S&S  S&S       S&S  S&S     S&S_sdSSS   
S&S     S&S  S&S    S&S  S&S       S&S  S&S     S&S~YSSY#b  
S&S     S&S  S&S    S&S  S&S       S&S  S&S     S&S    `S%  
S*S     S*S  S*S    d*S  S*b       d*S  S*b     S*S     S%  
S*S  .  S*S  S*S   .S*S  S*S.     .S*S  S*S.    S*S     S&  
S*S_sSs_S*S  S*S_sdSSS    SSSbs_sdSSS    SSSbs  S*S     S&  
SSS~SSS~S*S  SSS~YSSY      YSSP~YSSY      YSSP  S*S     SS  
                                                SP          
                                                Y
"""
e = """
/| s\  s\  .s5SSSs\   /SSSs.  .s        .s    s.  
s| SS\ SS| SS    SS| sS    SS. sS        sS    SS. 
sS S%S S%S SS    S%S sS    S%S sS        sS    S%S 
SS S%S S%S SS    S%S SS    S%S SS        SS    S%S 
SS S%S S%S SS    S%S SS    S%S SS        SSSSs.S:' 
SS S%S S%S SS    S%S SS    S%S SS        SS  "SS\  
SS `:; `:; SS    `:; SS    `:; SS        SS    `:; 
SS ;,. ;,. SS    ;,. SS    ;,. SS    ;,. SS    ;,. 
`:;;:'`::' ;;;;;;;;| `:;;;;;:' `:;;;;;:' :;    ;:'
"""
f = """
    :::       ::: :::::::::   ::::::::  :::        :::    ::: 
   :+:       :+: :+:    :+: :+:    :+: :+:        :+:   :+:   
  +:+       +:+ +:+    +:+ +:+    +:+ +:+        +:+  +:+     
 +#+  +:+  +#+ +#+    +:+ +#+    +:+ +#+        +#++:++       
+#+ +#+#+ +#+ +#+    +#+ +#+    +#+ +#+        +#+  +#+       
#+#+# #+#+#  #+#    #+# #+#    #+# #+#        #+#   #+#       
###   ###   #########   ########  ########## ###    ###
"""
banners = [a,b,c,d,e,f]
banner = random.choice(banners)
os.system('cls||clear')
print(Fore.BLUE+banner)

a_list = {"A": "@2#q", "B": "xF!9", "C": "*3rW", "D": "^jM6", "E": "$pL1", "F": "&8vN", "G": "Z@7b", "H": "*k0V", "I": "yR4$", "J": "+oQ1", "K": "D6uX", "L": "_eG9", "M": "P0f!", "N": "bF7W", "O": "mJ5#", "P": "lA8T", "Q": "hU3$", "R": "tC6@", "S": "zP2o", "T": "!k1N", "U": "wB8Y", "V": "iQ7@", "W": "rV5!", "X": "aT3z", "Y": "sL0#", "Z": "xM9Q", "a": "5wV*", "b": "!L9a", "c": "o8R#", "d": "k2$Q", "e": "fM3@", "f": "yZ5*", "g": "H0l@", "h": "G1x#", "i": "nP7#", "j": "C6v@", "k": "bL9*", "l": "tR2b", "m": "vA3#", "n": "T1z!", "o": "sY8f", "p": "qX4*", "q": "pB0#", "r": "mN7@", "s": "zD6!", "t": "cJ3q", "u": "iV1t", "v": "rK8b", "w": "pY6#", "x": "xM5@", "y": "hS9!", "z": "gQ2#", " ": "_._"}
b_list = {"A": "6^k*P", "B": "g!M9", "C": "tF3@", "D": "r@8Q", "E": "j5#A", "F": "$uL2", "G": "X0^N", "H": "zR4w", "I": "Q1!v", "J": "Y3zP", "K": "c7B@", "L": "_mF5", "M": "D9!h", "N": "bK2r", "O": "W6pN", "P": "zV3@", "Q": "xL7f", "R": "*J2u", "S": "V8o", "T": "k@1Y", "U": "qP4!", "V": "gR3@", "W": "aN6f", "X": "m2X", "Y": "t5Q", "Z": "o9#F", "a": "F!5n", "b": "zK9o", "c": "mT3#", "d": "hL2^", "e": "$r1A", "f": "g8Q", "g": "oB4*", "h": "y3w", "i": "X2z@", "j": "v9N", "k": "bD7#", "l": "eT6", "m": "C0p", "n": "f!Q", "o": "J1y", "p": "z6x", "q": "X4u", "r": "c9Y", "s": "L1!m", "t": "P8e", "u": "B2r", "v": "W5@q", "w": "o7X", "x": "aN9", "y": "G3u", "z": "tQ4#", " ": "_._"}
c_list = {"A": "$rQ7", "B": "@p1", "C": "sL0*", "D": "zB5", "E": "nG3^", "F": "yM4v", "G": "w0tN", "H": "X9b", "I": "R6p!", "J": "K2f", "K": "a0Y", "L": "t8z", "M": "uL3", "N": "zQ5#", "O": "h!B", "P": "j2X", "Q": "P0r", "R": "kF1@", "S": "v9W", "T": "G3v", "U": "zN2", "V": "m4T", "W": "J8Y", "X": "f7Q", "Y": "pR2@", "Z": "q5b", "a": "uF1", "b": "@rT", "c": "x9L", "d": "b3Y", "e": "s5G", "f": "p2#", "g": "mR8", "h": "yL1", "i": "W6p", "j": "J4X", "k": "v@7", "l": "aD0", "m": "F3q", "n": "oQ9", "o": "zB2", "p": "h3V", "q": "P4f", "r": "m1T", "s": "X7y", "t": "G9c", "u": "r5L", "v": "b6Q", "w": "j8A", "x": "n0P", "y": "k4W", "z": "tQ5", " ": "_._"}
d_list = {"A": "k#B", "B": "T7v", "C": "R0p", "D": "G9y", "E": "c2#", "F": "fV1", "G": "wN8", "H": "zR3", "I": "@5X", "J": "b0Y", "K": "q6L", "L": "D4r", "M": "m5V", "N": "n0Q", "O": "y7T", "P": "l2z", "Q": "i3C", "R": "W6b", "S": "j1f", "T": "Q9A", "U": "z5X", "V": "p3m", "W": "g7R", "X": "L0q", "Y": "u8P", "Z": "f2Y", "a": "m2@", "b": "X7r", "c": "Q9w", "d": "uF4", "e": "p1A", "f": "N8y", "g": "rQ2", "h": "L5b", "i": "y6T", "j": "wQ0", "k": "v3X", "l": "F9a", "m": "g7R", "n": "P0c", "o": "y2L", "p": "h9F", "q": "t4B", "r": "b6Z", "s": "vX5", "t": "Q2m", "u": "R0y", "v": "a7L", "w": "X9f", "x": "p3B", "y": "rQ1", "z": "t0M", " ": "_._"}
e_list = {"A": "b3G", "B": "@4t", "C": "N9r", "D": "a2Q", "E": "z6y", "F": "T7v", "G": "oB1", "H": "X3p", "I": "C0f", "J": "m2Q", "K": "y1N", "L": "u5X", "M": "p9L", "N": "r4V", "O": "wQ7", "P": "b2m", "Q": "h6P", "R": "Z3f", "S": "v0t", "T": "R8b", "U": "P9X", "V": "j1F", "W": "g2L", "X": "u7M", "Y": "q5B", "Z": "s8N", "a": "g7H","b": "q4N","c": "z8T","d": "m2F","e": "v5X","f": "p1J","g": "r9L","h": "o3P","i": "w6B","j": "t7Q","k": "x2V","l": "u4M","m": "y5R","n": "b9Z","o": "s8N","p": "k1X","q": "f3T","r": "c2J","s": "l7W","t": "a5Y","u": "n9F","v": "e6B","w": "h8M","x": "d4P","y": "j3V","z": "i7L", " ": "_._"}
vars_list = [a_list, b_list, c_list, d_list, e_list]

while True:
    scm = int(input(f"{Fore.BLUE}Seçenek: \n    1: {Fore.RESET}Şifrele\n    {Fore.BLUE}2: {Fore.RESET}Çöz\n        {Fore.BLUE}Seçim: {Fore.RESET}"))

    if scm == 1:
        def sifrele(metin, selected_var):
            crypted = ""
            for harf in metin:
                if harf in selected_var:
                    crypted += selected_var[harf]
                else:
                    crypted += harf
            return crypted

        os.system('cls||clear')
        yazi = input(Fore.BLUE + 'Şifrelenecek Yazı: ' + Fore.RESET)
        selected_var = random.choice(vars_list)
        ek = ""
        if   selected_var == a_list: ek = "!@#$_"
        elif selected_var == b_list: ek = "%^&*_"
        elif selected_var == c_list: ek = "/*(-_"
        elif selected_var == d_list: ek = "+=}(_"
        elif selected_var == e_list: ek = ";:<>_"
        os.system('cls||clear')
        print(f"{Fore.BLUE}Şifrelenmiş: {Fore.RESET}{ek}{sifrele(yazi, selected_var)}")
        time.sleep(15)
        os.system('cls||clear')

    elif scm == 2:
        def coz(yazi, ek, vars_list):
            decrypted = ""
            selected_var = None

            if   ek == "!@#$_": selected_var = a_list
            elif ek == "%^&*_": selected_var = b_list
            elif ek == "/*(-_": selected_var = c_list
            elif ek == "+=}(_": selected_var = d_list
            elif ek == ";:<>_": selected_var = e_list
            else:
                print(Fore.RED + "Geçersiz Şifreleme Formatı! "+Fore.RESET+"İlk 5 İşarete Dikkat Et!!!")
                time.sleep(5)
                os.system('cls||clear')
                return None

            inverted_var = {v: k for k, v in selected_var.items()}
            buffer = ""
            for char in yazi:
                buffer += char
                if buffer in inverted_var:
                    decrypted += inverted_var[buffer]
                    buffer = ""

            return decrypted

        os.system('cls||clear')
        sifreli_yazi = input(Fore.BLUE + 'Çözülecek Yazı: ' + Fore.RESET)
        ek = sifreli_yazi[:5]
        sifreli_yazi = sifreli_yazi[5:]
        cozulmus = coz(sifreli_yazi, ek, vars_list)
        if cozulmus is not None:
            os.system('cls||clear')
            print(f"\n{Fore.BLUE}Çözülmüş: {Fore.RESET}{cozulmus}")
            time.sleep(5)
            os.system('cls||clear')

    else:
        print(f"{Fore.RED}Geçersiz Seçim! (1/2)")
        time.sleep(1)
        os.system('cls||clear')
