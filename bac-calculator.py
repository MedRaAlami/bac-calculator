#settings#
import re

def getscore(prompt):
    try:
        score=float(input(prompt))
    except ValueError:
        print("404 :D ")
        quit()
    if not score >= 0 and score<= 20:
        quit()
    return score

def getchoice(prompt, valid_options):
    try:
        choice=int(input(prompt))
    except ValueError:
        print("404 :D ")
        quit()
    if choice not in valid_options:
        quit()
    return choice

def getname(prompt):
    while True:
        name=input(prompt).strip()
        if re.fullmatch(r"[A-Za-z][A-Za-z\s\-]*", name):
            return name
        else:
            quit()

#info personnel#

first_name=getname("Enter your first name: ")
last_name=getname("Enter your last name: ")

#1BAC#

major1bac=getchoice(
   """Which of the following major in the first year of baccalaureate:
1)Science [Science Math, Science Exp]
2)Economics and Management Sciences 
3)Science and technology [STE, STM]
""", [1,2,3])

if major1bac == 1:
   FR=getscore("Enter your french regional exam result: ")
   HG=getscore("Enter your histo-geo regional exam result: ")
   NCFs = FR * 4
   NCHGs = HG * 2
elif major1bac == 2:
   FR=getscore("Enter your french regional exam result: ")
   HG=getscore("Enter your histo-geo regional exam result: ")
   NCFe = FR * 3
   NCHGe = HG * 3
elif major1bac ==3:
   FR=getscore("Enter your french regional exam result: ")
   NCFst = FR * 4
    
II=getscore("Enter your islamics regional exam result: ")
AR=getscore("Enter your arabic regional exam result: ")
NCII = II * 2
NCA = AR * 2

if major1bac == 1:
   Tot_r = NCFs + NCHGs + NCII + NCA
   Regio = Tot_r/10
elif major1bac == 2:
   Tot_r = NCFe + NCHGe + NCII + NCA
   Regio = Tot_r/10
elif major1bac == 3:
   Tot_r = NCFst + NCII + NCA
   Regio = Tot_r/8

Regio = round(Regio, 2)
print("Your regional bac exam results: ", Regio)

#2BAC#

if major1bac == 1:
   majorscience=getchoice(
      """Which of the following science majors did you choose in the first year of the baccalaureate:
1)Mathematical sciences [Science Math]
2)Experimental sciences [Science Exp]
""", [1,2])

   if majorscience == 1:
      majorsm=getchoice(
         """Which stream within mathematical sciences did you choose in your second year of the baccalaureate:
1)Mathematical sciences A [SM A]
2)Mathematical sciences B [SM B]
""", [1,2])
      
      MATHsm=getscore("Enter your math national exam result: ")
      PCsm=getscore("Enter your physics and chemistry national exam result: ")
      NCMsm = MATHsm * 9
      NCPCsm = PCsm * 7

      if majorsm == 2:
         SIsm=getscore("Enter your engineering science national exam result: ")
         NCSIsm = SIsm * 3
      elif majorsm == 1:
         SVTsm=getscore("Enter your life and earth sciences national exam result: ")
         NCSVTsm = SVTsm * 3

   elif majorscience == 2:
      majorsexp=getchoice(
         """Which stream within experimental sciences did you choose in your second year of the baccalaureate:
1)Physical sciences [SPC]
2)Life and earth sciences [SVT]
3)Agronomic sciences [S.Agro]
""", [1,2,3])

      MATHsexp=getscore("Enter your math national exam result: ")
      NCMsexp = MATHsexp * 7   

      if majorsexp == 1:
         PCpc=getscore("Enter your physics and chemistry national exam result: ")
         SVTpc=getscore("Enter your life and earth sciences national exam result: ")
         NCPCpc = PCpc * 7
         NCSVTpc = SVTpc * 5
      elif majorsexp == 2:
         PCsvt=getscore("Enter your physics and chemistry national exam result: ")
         SVTsvt=getscore("Enter your life and earth sciences national exam result: ")
         NCPCsvt = PCsvt * 5
         NCSVTsvt = SVTsvt * 7
      elif majorsexp == 3:
         PCagro=getscore("Enter your physics and chemistry national exam result: ")
         SVTagro=getscore("Enter your life and earth sciences national exam result: ")
         SVA=getscore("Enter your plant and animal sciences national exam result: ")
         NCPCagro = PCagro * 5
         NCSVTagro = SVTagro * 5
         NCSVA = SVA *5
elif major1bac == 2:
   majoreco=getchoice(
      """(Which stream within economics and management sciences did you choose in your second year of the baccalaureate:
1)Economic sciences [SE]
2)Accounting management sciences [SGC]
""", [1,2])

   MATHeco=getscore("Enter your math national exam result: ")
   NCMeco = MATHeco * 4

   if majoreco == 1:
      CMFse=getscore("Enter your accounting and financial mathematics national exam result: ")
      ECOGENse=getscore("Enter your general economics and statistics national exam result: ")
      ORGAse=getscore("Enter your economics and administrative management of enterprises national exam result: ")
      NCCMFse = CMFse * 4
      NCECOGENse = ECOGENse *6
      NCORGAse = ORGAse * 3
   elif majoreco == 2:
      CMFsgc=getscore("Enter your accounting and financial mathematics national exam result: ")
      ECOGENsgc=getscore("Enter your general economics and statistics national exam result: ")
      ORGAsgc=getscore("Enter your economics and administrative management of enterprises national exam result: ")
      NCCMFsgc = CMFsgc * 6
      NCECOGENsgc = ECOGENsgc * 3
      NCORGAsgc = ORGAsgc * 6
elif major1bac == 3:
   majorst=getchoice(
      """Which stream within science and technology did you choose in your second year of the baccalaureate: 
1)Electrical science and technology
2)Mechanical science and technology
""", [1,2])
   
   MATHst=getscore("Enter your math national exam result: ")
   PCst=getscore("Enter your physics and chemistry national exam result: ")
   SIst=getscore("Enter your engineering science national exam result: ")
   NCMst = MATHst * 7
   NCPCst = PCst * 5
   NCSIst = SIst * 8
   
ANG=getscore("Enter your english national exam result: ")
PHILO=getscore("Enter your philo national exam result: ")
NCAN = ANG * 2
NCPH = PHILO * 2

if major1bac == 1:
   if majorscience == 1:
      if majorsm == 1:
         Tot_n = NCMsm + NCPCsm + NCSVTsm + NCAN + NCPH
         Natio = Tot_n/23
      elif majorsm == 2:
         Tot_n = NCMsm + NCPCsm + NCSIsm + NCAN + NCPH
         Natio = Tot_n/23
   elif majorscience == 2:
      if majorsexp == 1:
         Tot_n = NCMsexp + NCPCpc + NCSVTpc + NCAN + NCPH
         Natio = Tot_n/23
      elif majorsexp == 2:
         Tot_n = NCMsexp + NCPCsvt + NCSVTsvt + NCAN + NCPH
         Natio = Tot_n/23
      elif majorsexp == 3:
         Tot_n = NCMsexp + NCPCagro + NCSVTagro + NCSVA + NCAN + NCPH
         Natio = Tot_n/26
elif major1bac == 2:
   if majoreco == 1:
      Tot_n = NCMeco + NCCMFse + NCECOGENse + NCORGAse + NCAN + NCPH
      Natio = Tot_n/21
   elif majoreco == 2:
      Tot_n = NCMeco + NCCMFsgc + NCECOGENsgc + NCORGAsgc + NCAN + NCPH
      Natio = Tot_n/23
elif major1bac == 3:
   Tot_n = NCMst + NCPCst + NCSIst + NCAN + NCPH
   Natio = Tot_n/24

Natio = round(Natio, 2) 
print("Your national bac exam results:", Natio)

natio_scores = []
if major1bac == 1:
    if majorscience == 1:
        natio_scores.extend([MATHsm, PCsm])
        if majorsm == 1:
            natio_scores.append(SVTsm)
        elif majorsm == 2:
            natio_scores.append(SIsm)
        elif majorscience == 2:
            natio_scores.append(MATHsexp)
            if majorsexp == 1:
                natio_scores.extend([PCpc, SVTpc])
            elif majorsexp == 2:
                natio_scores.extend([PCsvt, SVTsvt])
            elif majorsexp == 3:
                natio_scores.extend([PCagro, SVTagro, SVA])
    elif major1bac == 2:
        natio_scores.append(MATHeco)
        if majoreco == 1:
            natio_scores.extend([CMFse, ECOGENse, ORGAse])
        elif majoreco == 2:
            natio_scores.extend([CMFsgc, ECOGENsgc, ORGAsgc])
    elif major1bac == 3:
        natio_scores.extend([MATHst, PCst, SIst])

    natio_scores.extend([ANG, PHILO])
    zero_natio = 0 in natio_scores

#moyenne générale#

QSTCC=getchoice(
        """Do you know your continuous assessment grade for the second year of the baccalaureate, or just your semester scores?
1)Yes, I know my continuous assessment grade
2)No, I only know my semester scores
""", [1, 2])

if QSTCC == 1:
    CC=getscore("Enter your continuous assessment grade for the second year of the baccalaureate: ")
elif QSTCC == 2:
    S1=getscore("Enter your first semester score: ")
    S2=getscore("Enter your second semester score: ")
    CC = (S1 + S2) / 2
    CC = round(CC, 2)
    print("Your continuous assessment is: ", CC)

MoyGen = ((2 * Natio) + Regio + CC) / 4
MoyGen = round(MoyGen, 2)

print(f"Full Name: {first_name} {last_name}")
print("Your overall baccalaureate average is: ", MoyGen)

if zero_natio:
    print("You have a 0 in one of the national exam subjects, to the remedial exam")
else:
    if MoyGen >= 10 and MoyGen < 12:
        print("Pass")
    elif MoyGen >= 12 and MoyGen < 14:
        print("Merit")
    elif MoyGen >= 14 and MoyGen < 16:
        print("Distinction")
    elif MoyGen >= 16:
        print("High distinction")
    elif MoyGen < 10 and MoyGen >= 7:
        print("To the remedial exam")
    elif MoyGen < 7:
        print("Repeating the second year of the baccalaureate")
