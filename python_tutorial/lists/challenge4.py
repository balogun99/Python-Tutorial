scores = ['Balogun - 5', 'Adamu - 5', 'Ibrahim - 4', 'Isa - 4', 'Ashama - 4']
avg = 0

for score in scores:
    x = int(score[len(score)-1])
    avg += x
    
avg /= len(scores)
print("The average score is: ", avg)