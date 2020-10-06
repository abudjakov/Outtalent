import os
import urllib.parse
import subprocess

# Array.from(document.querySelectorAll('tr>td:nth-child(2)')).map(v => parseInt(v.innerText)).join(',')

solved = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
          31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
          58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
          85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109,
          110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131,
          132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153,
          154, 155, 160, 162, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182,
          183, 184, 185, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205,
          206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227,
          228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 257, 258, 260, 262, 263, 264, 268,
          273, 274, 275, 278, 279, 282, 283, 284, 287, 289, 290, 292, 295, 297, 299, 300, 301, 303, 304, 306, 307, 309,
          310, 312, 313, 315, 316, 318, 319, 321, 322, 324, 326, 327, 328, 329, 330, 331, 332, 334, 335, 336, 337, 338,
          339, 341, 342, 343, 344, 345, 346, 347, 349, 350, 352, 354, 355, 357, 359, 363, 365, 367, 368, 371, 372, 373,
          374, 375, 376, 377, 378, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396,
          397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 409, 410, 412, 413, 414, 415, 416, 417, 419, 420, 421,
          423, 424, 427, 429, 430, 432, 433, 434, 435, 436, 437, 438, 440, 441, 442, 443, 445, 446, 447, 448, 449, 450,
          451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 466, 467, 468, 470, 472, 473, 474, 475,
          476, 477, 478, 479, 480, 481, 482, 483, 485, 486, 488, 491, 492, 493, 494, 495, 496, 500, 501, 502, 504, 506,
          507, 509, 511, 514, 517, 520, 521, 523, 530, 532, 535, 538, 541, 543, 546, 551, 552, 557, 559, 561, 563, 564,
          566, 572, 575, 577, 581, 584, 586, 587, 589, 590, 591, 594, 595, 596, 598, 599, 605, 606, 613, 617, 620, 627,
          628, 633, 637, 643, 645, 653, 654, 657, 661, 665, 669, 671, 674, 680, 682, 686, 687, 690, 693, 696, 697, 700,
          701, 703, 704, 705, 706, 707, 709, 717, 720, 724, 728, 732, 733, 744, 746, 747, 748, 760, 762, 763, 766, 771,
          773, 779, 783, 784, 788, 796, 797, 804, 806, 807, 811, 812, 814, 819, 821, 824, 830, 832, 836, 840, 844, 849,
          852, 859, 860, 861, 862, 867, 868, 872, 874, 876, 880, 883, 884, 888, 890, 892, 893, 894, 895, 896, 897, 905,
          908, 914, 917, 921, 922, 925, 929, 933, 937, 938, 941, 942, 944, 949, 950, 953, 961, 965, 970, 976, 977, 980,
          985, 989, 993, 997, 999, 1002, 1005, 1008, 1009, 1010, 1013, 1018, 1021, 1022, 1025, 1028, 1029, 1030, 1033,
          1037, 1038, 1042, 1046, 1047, 1050, 1051, 1068, 1069, 1071, 1074, 1078, 1079, 1082, 1085, 1086, 1089, 1096,
          1103, 1104, 1108, 1111, 1114, 1119, 1122, 1128, 1134, 1137, 1148, 1154, 1160, 1161, 1165, 1170, 1173, 1175,
          1179, 1180, 1184, 1185, 1189, 1200, 1207, 1213, 1217, 1221, 1232, 1237, 1250, 1251, 1252, 1255, 1260, 1261,
          1266, 1275, 1277, 1278, 1279, 1280, 1281, 1282, 1284, 1286, 1287, 1289, 1290, 1295, 1298, 1299, 1302, 1303,
          1304, 1305, 1309, 1313, 1314, 1315, 1317, 1320, 1323, 1325, 1327, 1329, 1331, 1332, 1337, 1342, 1346, 1347,
          1350, 1351, 1356, 1360, 1365, 1370, 1374, 1378, 1379, 1380, 1381, 1382, 1385, 1387, 1389, 1394, 1395, 1399,
          1402, 1403, 1407, 1408, 1409, 1411, 1413, 1415, 1417, 1420, 1422, 1431, 1435, 1436, 1439, 1441, 1442, 1446,
          1448, 1450, 1455, 1460, 1463, 1464, 1467, 1469, 1470, 1474, 1475, 1476, 1480, 1484, 1486, 1491, 1496, 1502,
          1507, 1511, 1512, 1517, 1518, 1523, 1527, 1528, 1529, 1534, 1539, 1544, 1550, 1551, 1556, 1560, 1561, 1565,
          1566, 1571, 1572, 1576, 1581, 1582, 1588, 1592, 1598, 1603, 1608}

secret_files = subprocess.Popen('git-crypt status -e',
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True).communicate()[0].decode('utf-8').splitlines()

secret_files = {x.replace('    encrypted: ', '').replace('../', '') for x in secret_files if 'README.md' in x}

dir_path = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(dir_path, '../'))

GIT_ULR_PREFIX = 'https://github.com/CrazySquirrel/Outtalent/tree/master'

SITES = ['Leetcode']

global_readme = [
    '# Algorithms, data structures and programming solutions.',
    ''
]

for site in SITES:
    site_path = os.path.join(root_path, site)

    site_readme = [
        '# %s' % (site),
        ''
    ]

    tasks = []

    for file in os.listdir(site_path):
        if os.path.isdir(os.path.join(site_path, file)):
            tasks.append(file)

    for task in sorted(tasks, key=lambda x: int(x.split('.')[0])):
        id = task.split('.')[0]
        if id.isnumeric():
            id = int(id)
            if id in solved: solved.remove(id)
        is_secret = ('%s/%s/README.md' % (site, task)) in secret_files
        if is_secret:
            site_readme.append('* ~~%s~~ (Secret)' % (task))
        else:
            site_readme.append('* [%s](%s/README.md)' % (task, urllib.parse.quote(task)))

    with open(os.path.join(site_path, 'README.md'), 'w') as readme:
        readme.write('\n'.join(site_readme))

if solved:
    print('Should be added: %s' % (', '.join(map(str, solved))))

print('README.md UPDATED!!!')
