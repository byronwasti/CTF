in_cards = ["bJoker","9d","4d","Qs","Qd","Kd","Ah","8s","10h","10d","rJoker","5d","10c","6h","9h","Jd","Ad","3h","3c","2s","6d","6s","7c","4c","4s","5s","7s","5h","Jh","2d","3d","8h","5c","Ks","Qh","7h","9s","8d","7d","8c","9c","2h","Js","Ac","Kh","3s","Jc","As","Kc","Qc","2c","6c","4h","10s"]

crypted = "ZOOIRAGJAKHITTEV"
print(crypted)
print(crypted[::-1])


def add_suit( string ):
    if "c" in string:
        return 0
    if "d" in string:
        return 13
    if "h" in string:
        return 26
    if "s" in string:
        return 39


def convert_cards( card_list ):
    out = []
    value = 0
    for i in card_list:
        value = 0
        if "Joker" in i:
            if "b" in i:
                out.append(54)
            elif "r" in i:
                out.append(53)
            else:
                raise Exception("Invalid joker")
            continue

        elif "J" in i:
            value = 11
        elif "Q" in i:
            value = 12
        elif "K" in i:
            value = 13
        elif "A" in i:
            value = 1
        else:
            value = int(''.join(x for x in i if x.isdigit()))

        value += add_suit( i )
        out.append(value)

    return out

if __name__ == "__main__":
    out = convert_cards( in_cards )
    test = [str(i) for i in out]
    comp = ['54','22','17','51','25','26','27','47','36','23','53','18','10','32','35','24','14','29','3','41','19','45','7','4','43','44','46','31','37','15','16','34','5','52','38','33','48','21','20','8','9','28','50','1','39','42','11','40','13','12','2','6','30','49']
    print(test == comp)
    print(','.join(test))
    print(','.join(comp[::-1]))