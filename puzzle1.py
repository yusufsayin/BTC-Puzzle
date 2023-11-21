import secp256k1 as ice
import random

adresler = ['1NBC8uXJy1GiJ6drkiZa1WuKn51ps7EPTv', '14u4nA5sugaswb6SZgn5av2vuChdMnD9E5', '19z6waranEf8CcP8FqNgdwUe1QRxvUNKBG', '14JHoRAdmJg3XR4RjMDh6Wed6ft6hzbQe9', '1FTpAbQa4h8trvhQXjXnmNhqdiGBd1oraE', '1AoeP37TmHdFh8uN72fu9AqgtLrUwcv2wJ', '1NgVmsCCJaKLzGyKLFJfVequnFW9ZvnMLN', '18192XpzzdDi2K11QVHR7td2HcPS6Qs5vg', '1LuUHyrQr8PKSvbcY1v1PiuGuqFjWpDumN', '13Q84TNNvgcL3HJiqQPvyBb9m4hxjS3jkV', '1MUJSJYtGPVGkBCTqGspnxyHahpt5Te8jy', '1CXvTzR6qv8wJ7eprzUKeWxyGcHwDYP1i2', '1FwZXt6EpRT7Fkndzv6K4b4DFoT4trbMrV', '18aNhurEAJsw6BAgtANpexk5ob1aGTwSeL', '1M7ipcdYHey2Y5RZM34MBbpugghmjaV89P', '19GpszRNUej5yYqxXoLnbZWKew3KdVLkXg', '1NevxKDYuDcCh1ZMMi6ftmWwGrZKC6j7Ux', '13N66gCzWWHEZBxhVxG18P8wyjEWF9Yoi1', '15MnK2jXPqTMURX4xC3h4mAZxyCcaWWEDD', '1CD91Vm97mLQvXhrnoMChhJx4TP9MaQkJo', '1QKBaU6WAeycb3DbKbLBkX7vJiaS8r42Xo', '1Fz63c775VV9fNyj25d9Xfw3YHE6sKCxbt', '1Ab4vzG6wEQBDNQM1B2bvUz4fqXXdFk2WT', '15nf31J46iLuK1ZkTnqHo7WgN5cARFK3RA', '1UDHPdovvR985NrWSkdWQDEQ1xuRiTALq', '16RGFo6hjq9ym6Pj7N5H7L1NR1rVPJyw2v', '13A3JrvXmvg5w9XGvyyR4JEJqiLz8ZySY3', '17uDfp5r4n441xkgLFmhNoSW1KWp6xVLD', '1KrU4dHE5WrW8rhWDsTRjR21r8t3dsrS3R', '16zRPnT8znwq42q7XeMkZUhb1bKqgRogyy', '1Fo65aKq8s8iquMt6weF1rku1moWVEd5Ua', '1Hz3uv3nNZzBVMXLGadCucgjiCs5W9vaGz', '1MZ2L1gFrCtkkn6DnTT2e4PFUTHw9gNwaj', '1G6EFyBRU86sThN3SSt3GrHu1sA7w7nzi4', '1AWCLZAjKbV1P7AHvaPNCKiB7ZWVDMxFiz', '1BkkGsX9ZM6iwL3zbqs7HWBV7SvosR6m8N', '1CdufMQL892A69KXgv6UNBD17ywWqYpKut', '1Me3ASYt5JCTAK2XaC32RMeH34PdprrfDx', '1GDSuiThEV64c166LUFC9uDcVdGjqkxKyh', '1GuBBhf61rnvRe4K8zu8vdQB3kHzwFqSy7', '1PJZPzvGX19a7twf5HyD2VvNiPdHLzm9F6', '1KNRfGWw7Q9Rmwsc6NT5zsdvEb9M2Wkj5Z', '1MnJ6hdhvK37VLmqcdEwqC3iFxyWH2PHUV', '174SNxfqpdMGYy5YQcfLbSTK3MRNZEePoy', '1NeGn21dUDDeqFQ63xb2SpgUuXuBLA4WT4', '18A7NA9FTsnJxWgkoFfPAFbQzuQxpRtCos', '1824ZJQ7nKJ9QFTRBqn7z7dHV5EGpzUpH3', '1GvgAXVCbA8FBjXfWiAms4ytFeJcKsoyhL', '1HB1iKUqeffnVsvQsbpC6dNi1XKbyNuqao', '15EJFC5ZTs9nhsdvSUeBXjLAuYq3SWaxTc', '18KsfuHuzQaBTNLASyj15hy4LuqPUo1FNB', '1EQJvpsmhazYCcKX5Au6AZmZKRnzarMVZu', '1AcAmB6jmtU6AiEcXkmiNE9TNVPsj9DULf', '1PXv28YxmYMaB8zxrKeZBW8dt2HK7RkRPX', '1CKCVdbDJasYmhswB6HKZHEAnNaDpK7W4n', '1JWnE6p6UN7ZJBN7TtcbNDoRcjFtuDWoNL', '1CaBVPrwUxbQYYswu32w7Mj4HR4maNoJSX', '18ywPwj39nGjqBrQJSzZVq2izR12MDpDr8', '15ANYzzCp5BFHcCnVFzXqyibpzgPLWaD8b', '1K6xGMUbs6ZTXBnhw1pippqwK6wjBWtNpL', '17Q7tuG2JwFFU9rXVj3uZqRtioH3mx2Jad', '1AE8NzzgKE7Yhz7BWtAcAAxiFMbPo82NB5', '1EzVHtmbN4fs4MiNk3ppEnKKhsmXYJ4s74', '19QciEHbGVNY4hrhfKXmcBBCrJSBZ6TaVt', '16AbnZjZZipwHMkYKBSfswGWKDmXHjEpSf', '1PxH3K1Shdjb7gSEoTX7UPDZ6SH4qGPrvq', '1K3x5L6G57Y494fDqBfrojD28UJv4s5JcK', '1CMq3SvFcVEcpLMuuH8PUcNiqsK1oicG2D', '14MdEb4eFcT3MVG5sPFG4jGLuHJSnt1Dk2', '13zYrYhhJxp6Ui1VV7pqa5WDhNWM45ARAC', '15qsCm78whspNQFydGJQk5rexzxTQopnHZ', '1ARk8HWJMn8js8tQmGUJeQHjSE7KRkn2t8', '15qF6X51huDjqTmF9BJgxXdt1xcj46Jmhb', '1Bxk4CQdqL9p22JEtDfdXMsng1XacifUtE', '1DJh2eHFYQfACPmrvpyWc8MSTYKh7w9eRF', '1FWGcVDK3JGzCC3WtkYetULPszMaK2Jksv', '12VVRNPi4SJqUTsp6FmqDqY5sGosDtysn4', '1JTK7s9YVYywfm5XUH7RNhHJH1LshCaRFR', '1PWo3JeB9jrGwfHDNpdGK54CRas7fsVzXU', '19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG', '1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ', '1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9', '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so']
loop = 0

while True:          
    loop += 1    
    sayi = random.randint(1,2**256)
    pub_key = ice.scalar_multiplication(sayi).hex()
    
    xsayi = pub_key[2:66]       
    #print(xsayi)
    ysayi = pub_key[-64:]
    #print(ysayi)
    
    basamak = -16
    while basamak >= -39:
    # 1 ile başlayanlar
        x0 = "1" + xsayi[basamak:]       
        x1 = "1" + ysayi[basamak:]
    # 2 ve 3 ile başlayanlar    
        x2 = "2" + xsayi[basamak:]
        x3 = "2" + ysayi[basamak:]
        x4 = "3" + xsayi[basamak:]
        x5 = "3" + ysayi[basamak:]
    # 4-5-6-7 ile başlayanlar
        x6  = "4" + xsayi[basamak:]
        x7  = "4" + ysayi[basamak:]
        x8  = "5" + xsayi[basamak:]
        x9  = "5" + ysayi[basamak:]
        x10 = "6" + xsayi[basamak:]
        x11 = "6" + ysayi[basamak:]
        x12 = "7" + xsayi[basamak:]
        x13 = "7" + ysayi[basamak:]
    # 8-9-a-b-c-d-e ile başlayanlar
        x14 = "8" + xsayi[basamak:]
        x15 = "8" + ysayi[basamak:]
        x16 = "9" + xsayi[basamak:]
        x17 = "9" + ysayi[basamak:]
        x18 = "a" + xsayi[basamak:]
        x19 = "a" + ysayi[basamak:]
        x20 = "b" + xsayi[basamak:]
        x21 = "b" + ysayi[basamak:]
        x22 = "c" + xsayi[basamak:]
        x23 = "c" + ysayi[basamak:]
        x24 = "d" + xsayi[basamak:]
        x25 = "d" + ysayi[basamak:]
        x26 = "e" + xsayi[basamak:]
        x27 = "e" + ysayi[basamak:]
        x28 = "f" + xsayi[basamak:]
        x29 = "f" + ysayi[basamak:]
        
        x0 = int(x0, 16)
        x1 = int(x1, 16)
        x2 = int(x2, 16)
        x3 = int(x3, 16)
        x4 = int(x4, 16)
        x5 = int(x5, 16)
        x6 = int(x6, 16)
        x7 = int(x7, 16)
        x8 = int(x8, 16)
        x9 = int(x9, 16)
        x10 = int(x10, 16)
        x11 = int(x11, 16)
        x12 = int(x12, 16)
        x13 = int(x13, 16)
        x14 = int(x14, 16)
        x15 = int(x15, 16)
        x16 = int(x16, 16)
        x17 = int(x17, 16)
        x18 = int(x18, 16)
        x19 = int(x19, 16)
        x20 = int(x20, 16)
        x21 = int(x21, 16)
        x22 = int(x22, 16)
        x23 = int(x23, 16)
        x24 = int(x24, 16)
        x25 = int(x25, 16)
        x26 = int(x26, 16)
        x27 = int(x27, 16)
        x28 = int(x28, 16)
        x29 = int(x29, 16)
        
        adresx0 =  ice.privatekey_to_address(0, True, x0)
        adresx1 =  ice.privatekey_to_address(0, True, x1)
        adresx2 =  ice.privatekey_to_address(0, True, x2)
        adresx3 =  ice.privatekey_to_address(0, True, x3)
        adresx4 =  ice.privatekey_to_address(0, True, x4)
        adresx5 =  ice.privatekey_to_address(0, True, x5)
        adresx6 =  ice.privatekey_to_address(0, True, x6)
        adresx7 =  ice.privatekey_to_address(0, True, x7)
        adresx8 =  ice.privatekey_to_address(0, True, x8)
        adresx9 =  ice.privatekey_to_address(0, True, x9)
        adresx10 =  ice.privatekey_to_address(0, True, x10)
        adresx11 =  ice.privatekey_to_address(0, True, x11)
        adresx12 =  ice.privatekey_to_address(0, True, x12)
        adresx13 =  ice.privatekey_to_address(0, True, x13)
        adresx14 =  ice.privatekey_to_address(0, True, x14)
        adresx15 =  ice.privatekey_to_address(0, True, x15)
        adresx16 =  ice.privatekey_to_address(0, True, x16)
        adresx17 =  ice.privatekey_to_address(0, True, x17)
        adresx18 =  ice.privatekey_to_address(0, True, x18)
        adresx19 =  ice.privatekey_to_address(0, True, x19)
        adresx20 =  ice.privatekey_to_address(0, True, x20)
        adresx21 =  ice.privatekey_to_address(0, True, x21)
        adresx22 =  ice.privatekey_to_address(0, True, x22)
        adresx23 =  ice.privatekey_to_address(0, True, x23)
        adresx24 =  ice.privatekey_to_address(0, True, x24)
        adresx25 =  ice.privatekey_to_address(0, True, x25)
        adresx26 =  ice.privatekey_to_address(0, True, x26)
        adresx27 =  ice.privatekey_to_address(0, True, x27)
        adresx28 =  ice.privatekey_to_address(0, True, x28)
        adresx29 =  ice.privatekey_to_address(0, True, x29)
        if adresx0 in adresler:
            print(x0)
            exit()
        if adresx1 in adresler:
            print(x1)
            exit()
        if adresx2 in adresler:
            print(x2)
            exit()
        if adresx3 in adresler:
            print(x3)
            exit()
        if adresx4 in adresler:
            print(x4)
            exit()
        if adresx5 in adresler:
            print(x5)
            exit()
        if adresx6 in adresler:
            print(x6)
            exit()
        if adresx7 in adresler:
            print(x7)
            exit()
        if adresx8 in adresler:
            print(x8)
            exit()
        if adresx9 in adresler:
            print(x9)
            exit()
        if adresx10 in adresler:
            print(x10)
            exit()
        if adresx11 in adresler:
            print(x11)
            exit()
        if adresx12 in adresler:
            print(x12)
            exit()
        if adresx13 in adresler:
            print(x13)
            exit()
        if adresx14 in adresler:
            print(x14)
            exit()
        if adresx15 in adresler:
            print(x15)
            exit()
        if adresx16 in adresler:
            print(x16)
            exit()
        if adresx17 in adresler:
            print(x17)
            exit()
        if adresx18 in adresler:
            print(x18)
            exit()
        if adresx19 in adresler:
            print(x19)
            exit()
        if adresx20 in adresler:
            print(x20)
            exit()
        if adresx21 in adresler:
            print(x21)
            exit()
        if adresx22 in adresler:
            print(x22)
            exit()
        if adresx23 in adresler:
            print(x23)
            exit()
        if adresx24 in adresler:
            print(x24)
            exit()
        if adresx25 in adresler:
            print(x25)
            exit()
        if adresx26 in adresler:
            print(x26)
            exit()
        if adresx27 in adresler:
            print(x27)
            exit()
        if adresx28 in adresler:
            print(x28)
            exit()
        if adresx29 in adresler:
            print(x29)
            exit()
        
        basamak = basamak - 1
    
    
    
    print(f'[Loop: {loop}]', end='\r')
