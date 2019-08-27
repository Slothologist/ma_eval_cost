

pipeline = 'pipeline5'

times = []
amount_of_correct_recognitions = 0
amount_of_samples = 0
max_time = 0.
min_time = 1000000.

with open('saved_time/' + pipeline + '/p2.txt', 'r') as file:
    chunked = file.read().split('\n\n')
    chunked_lines = [chunk.strip().split('\n') for chunk in chunked]

    amount_of_samples = len(chunked)
    correct_recognitions = [x for x in chunked_lines if not 'no' in x[0]]
    amount_of_correct_recognitions = len(correct_recognitions)

    for chunk in correct_recognitions:
        time = float(chunk[1].split(' ')[1])
        times.append(time)
        if time > max_time:
            max_time = time
        if time < min_time:
            min_time = time


fraction_of_correct_recognitions = amount_of_correct_recognitions / float(amount_of_samples)
print('Number correct recognitions ' + str(amount_of_correct_recognitions))
print('Fraction of correct recognitions: ' + str(fraction_of_correct_recognitions))
print('Mean time for recognition: ' + str((sum(times))/amount_of_correct_recognitions))
print('Min time: ' + str(min_time))
print('Max time: ' + str(max_time))