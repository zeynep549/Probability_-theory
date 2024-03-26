import numpy as np
import matplotlib.pyplot as plt





def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def comb(n, r):
    return fac(n) // (fac(r) * fac(n - r))
def pc(t):
    return 0.6 + (2 * t - 40) / 1000

def pw(t):
    return 0.2 + (30 - t) / 1000

def pb(t):
    return 1 - (pc(t) + pw(t))
def pmf(k, n, p):
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))



num_questions = 100
time_full = 200  
p_correct = pc(time_full)
p_wrong = pw(time_full)
p_blank = pb(time_full)


x_values = np.arange(num_questions+1)
px = [pmf(k, num_questions, p_correct) for k in range(num_questions + 1)]
py = [pmf(k, num_questions, p_wrong) for k in range(num_questions + 1)]
pz = [pmf(k, num_questions, p_blank) for k in range(num_questions + 1)]


plt.figure(figsize=(30, 5))


plt.subplot(1, 3, 1)
plt.bar(x_values, px, width=1, label='Correct Answer Probability ', color='blue')
plt.title('PMF of X (Correct Answers)')
plt.xlabel('Number of Correct Answers')
plt.ylabel('Probability')
plt.grid(True)
plt.legend()
plt.savefig('c:/Users/user/OneDrive/Masaüstü/pxpmf.png')
#plt.show()
# PMF of Y
plt.subplot(1, 3, 2)
plt.bar(x_values, py, width=1, label='Wrong Answer Probability ', color='red')
plt.title('PMF of Y (Wrong Answers)')
plt.xlabel('Number of Wrong Answers')
plt.grid(True)
plt.legend()
plt.savefig('c:/Users/user/OneDrive/Masaüstü/pypmf.png')
#plt.show()

# PMF of Z
plt.subplot(1, 3, 3)
plt.bar(x_values, pz, width=1, label='Blank Answer Probability', color='green')
plt.title('PMF of Z (Blank Answers)')
plt.xlabel('Number of Blank Answers')
plt.grid(True)
plt.legend()
plt.savefig('c:/Users/user/OneDrive/Masaüstü/pzpmf.png')
#plt.show()


#px_filename = 'c:/Users/user/OneDrive/Masaüstü/pxpmf.png'
#py_filename = 'c:/Users/user/OneDrive/Masaüstü/pypmf.png'
#pz_filename = 'c:/Users/user/OneDrive/Masaüstü/pzpmf.png'
#plt.savefig(px_filename)
#plt.savefig(py_filename)
#plt.savefig(pz_filename)




def get_net_points(correct, wrong):
    
    net_correct = correct - (wrong / 4)
    
    net_correct = max(net_correct, 0)
   
    return net_correct * 5






M = int(input("Enter the value of M (between 0 and 500): "))


probability_more_than_M = 0


for correct in range(num_questions + 1):
    for wrong in range(num_questions - correct + 1):
        net_p = get_net_points(correct, wrong)
        if net_p > M:
            prob = (comb(num_questions, correct) *
                    comb(num_questions - correct, wrong) *
                    (p_correct ** correct) *
                    (p_wrong ** wrong) *
                    (p_blank ** (num_questions - correct - wrong)))
            probability_more_than_M += prob

print( "b) mtMor400 ",  probability_more_than_M)
net_correct_needed = 40
current_net_correct = 20 - 7 / 4  

questions_left = num_questions - (20 + 7 + 4)


s = 0  

for additional_correct in range(questions_left + 1):
     for additional_incorrect in range(questions_left- additional_correct + 1):
    
        net_correct = current_net_correct + additional_correct - additional_incorrect / 4
        if net_correct >= net_correct_needed:
       
            prob = (comb(questions_left, additional_correct) *comb(questions_left-additional_correct,additional_incorrect)*
                (pc(120) ** additional_correct) *
                (pw(120) ** (additional_incorrect))*(pb(120) ** (questions_left - additional_correct - additional_incorrect)))
            s += prob

print("c) s " , s)
new_prob = 0
for correct in range(num_questions + 1):
    for wrong in range(num_questions - correct + 1):
        net_p = get_net_points(correct, wrong)
        if net_p > M and num_questions-correct-wrong>=8:
            prob = (comb(num_questions, correct) *
                    comb(num_questions - correct, wrong) *
                    (p_correct ** correct) *
                    (p_wrong ** wrong) *
                    (p_blank ** (num_questions - correct - wrong)))
            new_prob+= prob
if(new_prob != probability_more_than_M):
    print("d) news:" , new_prob)
break_time_phase1 = 4  
break_time_phase2 = 6 
p_correct_phase1 = pc(200)
p_incorrect_phase1 = pw(200)
p_correct_phase2 = pc(156)
p_incorrect_phase2 =  pw(156)
p_correct_phase3 = pc(110)
p_incorrect_phase3 = pw(110)
p_blank_phase1 = pb(200)
p_blank_phase2 = pb(156)
p_blank_phase3 = pb(110)
#print(comb(20, 10) * comb(10, 5) *(p_correct_phase1 ** 10) * ((p_incorrect_phase1) ** (5)*(p_blank_phase1)**(5)))
#print((comb(30, 10) * comb(20, 15) * (p_correct_phase2 ** 10) * ((p_incorrect_phase2) ** (15)*(p_blank_phase2)**(5))))
#print( (comb(50, 25) * comb(25, 15) * (p_correct_phase3 ** 25) * ((p_incorrect_phase3) ** (15)*(p_blank_phase3)**(10))))


def calculate_probability_less_than_300(p_correct_phase1, p_correct_phase2, p_correct_phase3, break_time_phase1, break_time_phase2):
    total_probability = 0
    
    for correct_phase1 in range(21):  
        for correct_phase2 in range(31):  
            for correct_phase3 in range(51):  
                for incorrect_phase1 in range(21-correct_phase1):
                    for incorrect_phase2 in range(31-correct_phase2):
                        for incorrect_phase3 in range(51-correct_phase3):
                            total_points = get_net_points(correct_phase1, incorrect_phase1) + get_net_points(correct_phase2, incorrect_phase2) + get_net_points(correct_phase3, incorrect_phase3)
                if total_points < 300:
                        prob_combination = (comb(20, correct_phase1) * comb(20 - correct_phase1, incorrect_phase1) * (p_correct_phase1 ** correct_phase1) * ((p_incorrect_phase1) ** (incorrect_phase1) * (p_blank_phase1) ** (20 - incorrect_phase1 - correct_phase1))) * \
                                                   (comb(30, correct_phase2) * comb(30 - correct_phase2, incorrect_phase2) * (p_correct_phase2 ** correct_phase2) * ((p_incorrect_phase2) ** (incorrect_phase2) * (p_blank_phase2) ** (30 - incorrect_phase2 - correct_phase2))) * \
                                                   (comb(50, correct_phase3) * comb(50 - correct_phase3, incorrect_phase3) * (p_correct_phase3 ** correct_phase3) * ((p_incorrect_phase3) ** (incorrect_phase3) * (p_blank_phase3) ** (50 - incorrect_phase3 - correct_phase3)))
                        total_probability += prob_combination
    
    return total_probability









probability_less_than_300 = calculate_probability_less_than_300(p_correct_phase1, p_correct_phase2, p_correct_phase3, break_time_phase1, break_time_phase2)
print("e) lt300:" ,probability_less_than_300)


lam = 1 / 40


n = 2  

x = np.linspace(0, 200, 1000)  


def erlang_pdf(n, lam, x):
    return (lam**n * x**(n-1) * np.exp(-lam * x)) / np.math.factorial(n-1)

pdf_values = erlang_pdf(2, 1/40, x)





#plt.show()


probability_between_60_80 = np.trapz(pdf_values[(x >= 60) & (x <= 80)], x[(x >= 60) & (x <= 80)])
print("g) b6080", probability_between_60_80)