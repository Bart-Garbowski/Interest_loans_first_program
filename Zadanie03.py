
January_01_2020 = 1.59282448436825
February_02_2020 = -0.453509101198007
March_03_2020 = 2.32467171712441
April_04_2020 = 1.26125440724877
May_05_2020 = 1.78252628571251
June_06_2020 = 2.32938454145522
July_07_2020 = 1.50222984223283
August_08_2020 = 1.78252628571251
September_09_2020 = 2.32884899407637
October_10_2020 = 0.616921348207244
November_11_2020 = 2.35229588637833
December_12_2020 = 0.337779545187098
January_01_2021 = 1.57703524727525
February_02_2021 = -0.292781442607648
March_03_2021 = 2.48619659017508
April_04_2021 = 0.267110317834564
May_05_2021 = 1.41795267229799
June_06_2021 = 1.05424326726375
July_07_2021 = 1.4805201044812
August_08_2021 = 1.57703524727525
September_09_2021 = -0.0774206903147018
October_10_2021 = 1.16573339872354
November_11_2021 = -0.404186717638335
December_12_2021 = 1.49970852083123

print("Hello")
name = input("What's your name? ")
print("Nice to meet you " + name + ", Im your loan calculator bot")

print("I will need a bit of data to help you calculate your loan for following 24 months")
loan_amount = float(input("Please tell me what is your loan amount? "))

interest_rate = float(input("Now tell me, please, your interest rate without percentage sign "))

monthly_payment = float(input("And the last thing please tell me what you want to pay by month? "))


January_final_20 = float(1 + ((January_01_2020 + interest_rate) / loan_amount)) * loan_amount - monthly_payment
February_final_20 = float(1 + ((February_02_2020 + interest_rate) / loan_amount)) * January_final_20 - monthly_payment
March_final_20 = float(1 + ((March_03_2020 + interest_rate) / loan_amount)) * February_final_20 - monthly_payment
April_final_20 = float(1 + ((April_04_2020 + interest_rate) / loan_amount)) * March_final_20 - monthly_payment
May_final_20 = float(1 + ((May_05_2020 + interest_rate) / loan_amount)) * April_final_20 - monthly_payment
June_final_20 = float(1 + ((June_06_2020 + interest_rate) / loan_amount)) * May_final_20 - monthly_payment
July_final_20 = float(1 + ((July_07_2020 + interest_rate) / loan_amount)) * June_final_20 - monthly_payment
August_final_20 = float(1 + ((August_08_2020 + interest_rate) / loan_amount)) * July_final_20 - monthly_payment
September_final_20 = float(1 + ((September_09_2020 + interest_rate) / loan_amount)) * August_final_20 - monthly_payment
October_final_20 = float(1 + ((October_10_2020 + interest_rate) / loan_amount)) * September_final_20 - monthly_payment
November_final_20 = float(1 + ((November_11_2020 + interest_rate) / loan_amount)) * October_final_20 - monthly_payment
December_final_20 = float(1 + ((December_12_2020 + interest_rate) / loan_amount)) * November_final_20 - monthly_payment
January_final_21 = float(1 + ((January_01_2021 + interest_rate) / loan_amount)) * December_final_20 - monthly_payment
February_final_21 = float(1 + ((February_02_2021 + interest_rate) / loan_amount)) * January_final_21 - monthly_payment
March_final_21 = float(1 + ((March_03_2021 + interest_rate) / loan_amount)) * February_final_21 - monthly_payment
April_final_21 = float(1 + ((April_04_2021 + interest_rate) / loan_amount)) * March_final_21 - monthly_payment
May_final_21 = float(1 + ((May_05_2021 + interest_rate) / loan_amount)) * April_final_21 - monthly_payment
June_final_21 = float(1 + ((June_06_2021 + interest_rate) / loan_amount)) * May_final_21 - monthly_payment
July_final_21 = float(1 + ((July_07_2021 + interest_rate) / loan_amount)) * June_final_21 - monthly_payment
August_final_21 = float(1 + ((August_08_2021 + interest_rate) / loan_amount)) * July_final_21 - monthly_payment
September_final_21 = float(1 + ((September_09_2021 + interest_rate) / loan_amount)) * August_final_21 - monthly_payment
October_final_21 = float(1 + ((October_10_2021 + interest_rate) / loan_amount)) * September_final_21 - monthly_payment
November_final_21 = float(1 + ((November_11_2021 + interest_rate) / loan_amount)) * October_final_21 - monthly_payment
December_final_21 = float(1 + ((December_12_2021 + interest_rate) / loan_amount)) * November_final_21 - monthly_payment

text1 = "Your outstanding loan amount is"
text2 = "its"
text3 = "less than the previous month."

final_1_20 = (round(January_final_20, 2))
less1 = float(round(loan_amount - January_final_20))
final_2_20 = (round(February_final_20, 2))
less2 = float(round(January_final_20 - February_final_20))
final_3_20 = (round(March_final_20, 2))
less3 = float(round(February_final_20 - March_final_20))
final_4_20 = (round(April_final_20, 2))
less4 = float(round(March_final_20 - April_final_20))
final_5_20 = (round(May_final_20, 2))
less5 = float(round(April_final_20 - May_final_20))
final_6_20 = (round(June_final_20, 2))
less6 = float(round(May_final_20 - June_final_20))
final_7_20 = (round(July_final_20, 2))
less7 = float(round(June_final_20 - July_final_20))
final_8_20 = (round(August_final_20, 2))
less8 = float(round(July_final_20 - August_final_20))
final_9_20 = (round(September_final_20, 2))
less9 = float(round(August_final_20 - September_final_20))
final_10_20 = (round(October_final_20, 2))
less10 = float(round(September_final_20 - October_final_20))
final_11_20 = (round(November_final_20, 2))
less11 = float(round(October_final_20 - November_final_20))
final_12_20 = (round(December_final_20, 2))
less12 = float(round(November_final_20 - December_final_20))

final_1_21 = (round(January_final_21, 2))
less13 = float(round(December_final_20 - January_final_21))
final_2_21 = (round(February_final_21, 2))
less14 = float(round(January_final_21 - February_final_21))
final_3_21 = (round(March_final_21, 2))
less15 = float(round(February_final_21 - March_final_21))
final_4_21 = (round(April_final_21, 2))
less16 = float(round(March_final_21 - April_final_21))
final_5_21 = (round(May_final_21, 2))
less17 = float(round(April_final_21 - May_final_21))
final_6_21 = (round(June_final_21, 2))
less18 = float(round(May_final_21 - June_final_21))
final_7_21 = (round(July_final_21, 2))
less19 = float(round(June_final_21 - July_final_21))
final_8_21 = (round(August_final_21, 2))
less20 = float(round(July_final_21 - August_final_21))
final_9_21 = (round(September_final_21, 2))
less21 = float(round(August_final_21 - September_final_21))
final_10_21 = (round(October_final_21, 2))
less22 = float(round(September_final_21 - October_final_21))
final_11_21 = (round(November_final_21, 2))
less23 = float(round(October_final_21 - November_final_21))
final_12_21 = (round(December_final_21, 2))
less24 = float(round(November_final_21 - December_final_21))


print(f'{text1} {final_1_20} {text2} {less1} {text3}')
print(f'{text1} {final_2_20} {text2} {less2} {text3}')
print(f'{text1} {final_3_20} {text2} {less3} {text3}')
print(f'{text1} {final_4_20} {text2} {less4} {text3}')
print(f'{text1} {final_5_20} {text2} {less5} {text3}')
print(f'{text1} {final_6_20} {text2} {less6} {text3}')
print(f'{text1} {final_7_20} {text2} {less7} {text3}')
print(f'{text1} {final_8_20} {text2} {less8} {text3}')
print(f'{text1} {final_9_20} {text2} {less9} {text3}')
print(f'{text1} {final_10_20} {text2} {less10} {text3}')
print(f'{text1} {final_11_20} {text2} {less11} {text3}')
print(f'{text1} {final_12_20} {text2} {less12} {text3}')

print(f'{text1} {final_1_21} {text2} {less13} {text3}')
print(f'{text1} {final_2_21} {text2} {less14} {text3}')
print(f'{text1} {final_3_21} {text2} {less15} {text3}')
print(f'{text1} {final_4_21} {text2} {less16} {text3}')
print(f'{text1} {final_5_21} {text2} {less17} {text3}')
print(f'{text1} {final_6_21} {text2} {less18} {text3}')
print(f'{text1} {final_7_21} {text2} {less19} {text3}')
print(f'{text1} {final_8_21} {text2} {less20} {text3}')
print(f'{text1} {final_9_21} {text2} {less21} {text3}')
print(f'{text1} {final_10_21} {text2} {less22} {text3}')
print(f'{text1} {final_11_21} {text2} {less23} {text3}')
print(f'{text1} {final_12_21} {text2} {less24} {text3}')

