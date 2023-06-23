# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 
# 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 
# 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.

S = [["ObjectOrientedProgramming1", 3.0, "A+"],
    ["IntroductiontoComputerEngineering", 3.0, "A+"],
    ["ObjectOrientedProgramming2" ,3.0, "A0"],
    ["CreativeComputerEngineeringDesign" ,3.0, "A+"],
    ["AssemblyLanguage" ,3.0, "A+"],
    ["InternetProgramming" ,3.0, "B0"],
    ["ApplicationProgramminginJava" ,3.0, "A0"],
    ["SystemProgramming" ,3.0, "B0"],
    ["OperatingSystem" ,3.0, "B0"], 
    ["WirelessCommunicationsandNetworking" ,3.0, "C+"],
    ["LogicCircuits" ,3.0, "B0"],
    ["DataStructure" ,4.0, "A+"],
    ["MicroprocessorApplication" ,3.0, "B+"],
    ["EmbeddedSoftware" ,3.0, "C0"],
    ["ComputerSecurity" ,3.0, "D+"],
    ["Database" ,3.0, "C+"],
    ["Algorithm" ,3.0, "B0"],
    ["CapstoneDesigninCSE" ,3.0, "B+"],
    ["CompilerDesign" ,3.0, "D0"],
    ["ProblemSolving" ,4.0, "P"]]   

total = 0
total_c = 0
for num in range(20):
    S = list(map(str, input().split()))
    
    credit = float(S[1])
    score = S[2]
    
    if score == "A+":
        score = 4.5
    elif score == "A0":
        score = 4.0
    elif score == "B+":
        score = 3.5
    elif score == "B0":
        score = 3.0
    elif score == "C+":
        score = 2.5
    elif score == "C0":
        score = 2.0
    elif score == "D+":
        score = 1.5
    elif score == "D0":
        score = 1.0
    elif score == "F":
        score = 0
    elif score == "P":
        score = 0
        total_c -=credit
        
        
    total_c += credit
    total += (credit*score)
        
avg = total/total_c
print(avg)
    
    