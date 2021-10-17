def create_palindrome(string, size):
    iterations = len(string) - size + 1

    for start_index in range(0, iterations):
        # print("start_index: " + str(start_index) + " char: " + string[start_index])

        normal_word = string[start_index:start_index+size]
        reversed_word = normal_word[len(normal_word):0:-1] + normal_word[0]
        # print("normal: " + normal_word)
        # print("reversed: " + reversed_word)

        if normal_word == reversed_word:
            return normal_word


def find_palindromes(string):

    for i in range(0, len(string)):
        # print("Creating palindromes of size: " + str(len(string)-i))
        longest_palindrome = create_palindrome(string=string, size=len(string)-i)

        if longest_palindrome is not None:
            print(longest_palindrome + " of size " + str(len(longest_palindrome)))
            break


if __name__ == '__main__':
    palindrome = """Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceiv
edinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedi
nagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlo
ngendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionoft
hatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisalto
getherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotco
nsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveco
nsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongre
memberwhatwesayherebutitcanneverracecareattheydidhereItisforusthelivingrathertobed
edicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedI
tisratherforustoracecarebeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonore
ddeadwetakeincreaseddevotitattarrattat
causeforwhichtheygavethelastpfullmeasureofdevoti
onthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGod
shallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeoplesh
allnotperishfromtheearth"""

    find_palindromes(palindrome)
