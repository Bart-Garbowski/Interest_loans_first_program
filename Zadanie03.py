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


#print("Hello")
#name = input("What's your name? ")
#print("Nice to meet you " + name + ", Im your loan calculator bot")


#print("I will need a bit of data to help you calculate your loan")
#loan_amount = input("Please tell me what is your loan amount? ")

#interest_rate = input("Now tell me, please, your interest rate without percentage sign ")

#monthly_payment = input("And the last thing please tell me what you want to pay by month? ")

loan_amount = 12000

January_rate_2020 = float(1 + ((float(January_01_2020) + 3 ) / loan_amount)) * loan_amount - 200

print(round(January_rate_2020, 5))
