
def get_diff_once(tup):
    bot = abs(tup[0]-tup[2]), abs(tup[1]-tup[2])
    top = abs(tup[0]-(tup[2]+360)), abs(tup[1]-(tup[2]+360))
    mini = min(bot[0], top[0]), min(bot[1], top[1])
    return sum(mini)/2.

pipeline1_old_info = [(109, 160,  90), (159, 198, 180), (194, 161, 270), (158, 185, 0), (188, 180, 90 )]
diffs = [get_diff_once(x) for x in pipeline1_old_info]
print('run 1 old pipeline: ' + str(sum(diffs)/len(diffs)))

pipeline1_new_info = [(134, 115,  90), (0, 0, 180), (171, 223, 270), (267, 259, 0), (122, 154, 90 )]
diffs = [get_diff_once(x) for x in pipeline1_new_info]
print('run 1 new pipeline: ' + str(sum(diffs)/len(diffs)))
print('--------------------------------')

pipeline2_old_info = [(157, 235, 270), (189, 180, 0), (154, 171, 90), (173, 149, 180), (141, 160, 270)]
diffs = [get_diff_once(x) for x in pipeline2_old_info]
print('run 2 old pipeline: ' + str(sum(diffs)/len(diffs)))

pipeline2_new_info = [(224, 273, 270), (260, 253, 0), (92, 141, 90), (234, 192, 180), ( 260, 189, 270)]
diffs = [get_diff_once(x) for x in pipeline2_new_info]
print('run 2 new pipeline: ' + str(sum(diffs)/len(diffs)))
print('--------------------------------')

pipeline4_old_info = [(179, 198, 0), (178, 187, 90), (270, 211, 180), (198, 159, 270), (192, 162, 0)]
diffs = [get_diff_once(x) for x in pipeline4_old_info]
print('run 4 old pipeline: ' + str(sum(diffs)/len(diffs)))

pipeline4_new_info = [(275, 229, 0), (126, 130, 90), (138,  0 , 180), (239, 201, 270), (207, 248, 0)]
diffs = [get_diff_once(x) for x in pipeline4_new_info]
print('run 4 new pipeline: ' + str(sum(diffs)/len(diffs)))
print('--------------------------------')

pipeline5_old_info = [(132, 163, 180), (177, 134, 270), (161, 181, 0), (171, 172, 90), (193, 354, 180)]
diffs = [get_diff_once(x) for x in pipeline5_old_info]
print('run 5 old pipeline: ' + str(sum(diffs)/len(diffs)))

pipeline5_new_info = [(135, 199, 180), (185, 220, 270), (273, 313, 0), (86, 102, 90), (194, 0 , 180)]
diffs = [get_diff_once(x) for x in pipeline5_new_info]
print('run 5 new pipeline: ' + str(sum(diffs)/len(diffs)))
print('--------------------------------')

pipeline6_old_info = [(141, 205, 0), (215, 147, 90), (182, 162, 180), (151, 266, 270), (176, 179, 0)]
diffs = [get_diff_once(x) for x in pipeline6_old_info]
print('run 6 old pipeline: ' + str(sum(diffs)/len(diffs)))

pipeline6_new_info = [(290, 331 , 0), (161,  83, 90), (0, 0, 180), (178, 316, 270), (302, 270, 0)]
diffs = [get_diff_once(x) for x in pipeline6_new_info]
print('run 6 new pipeline: ' + str(sum(diffs)/len(diffs)))
print('--------------------------------')

pipeline7_old_info = [(202, 196, 0), (167, 153, 90), (194, 167, 180), (161, 166, 270), (178, 188, 0)]
diffs = [get_diff_once(x) for x in pipeline7_old_info]
print('run 7 old pipeline: ' + str(sum(diffs)/len(diffs)))

pipeline7_new_info = [(323, 348, 0), (98, 143, 90), (216,  0 , 180), (235, 229, 270), (331, 272, 0)]
diffs = [get_diff_once(x) for x in pipeline7_new_info]
print('run 7 new pipeline: ' + str(sum(diffs)/len(diffs)))

