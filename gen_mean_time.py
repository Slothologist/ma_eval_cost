

pipeline = 'pipeline2'

times = []
amount_of_correct_recognitions = 0
amount_of_samples = 0

with open('saved_time/' + pipeline + '/p2.txt', 'r') as file:
    chunked = file.read().split('\n\n')
    chunked_lines = [chunk.strip().split('\n') for chunk in chunked]

    amount_of_samples = len(chunked)
    correct_recognitions = [x for x in chunked_lines if not 'no' in x[0]]
    amount_of_correct_recognitions = len(correct_recognitions)

    for chunk in correct_recognitions:
        times.append(float(chunk[1].split(' ')[1]))


fraction_of_correct_recognitions = amount_of_correct_recognitions / float(amount_of_samples)
print('Fraction of correct recognitions: ' + str(fraction_of_correct_recognitions))
print('Mean time for recognition: ' + str(sum(times)/amount_of_correct_recognitions))