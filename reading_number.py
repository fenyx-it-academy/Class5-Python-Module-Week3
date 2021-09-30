def reading_number(sayı):
        F={'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
        S={'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen','16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen'}
        T={"2": 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy','8': 'Eighty', '9': 'Ninety'}
        sayı=str(sayı)
        if len(sayı) == 2:
                if 10 <= int(sayı) <= 19:
                        print(S[sayı])
                elif sayı[1] == '0':
                        print(T[sayı[0]])
                else :
                        print( f"{T[sayı[0]]} {F[sayı[1]]}" )
        return ('Please enter a two-digit number')

reading_number(35)