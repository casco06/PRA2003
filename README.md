# PRA2003
Name: Cas Coolen
Student ID: i6413130
Chemistry Themed Project 
Questions:
-1: What are the average counts of each molecular species
and their statistical uncertainties?
-2: Is there any asymmetry between the normal and the
variant molecule?
-3: Is there any asymmetry as a function of their momentum?

Question 1:
The values below are the weigthed averages of the occurence of each molecule ID across 5M events split into 10 subsamples.
The uncertainty was calculated by taking the standard deviation of the means for all subsamples.

Results:
3222: 0.14953040315799693 +/- 0.0006063822903933391
-3122: 0.27169916728644494 +/- 0.0009348123674006773
211: 19.949556308899368 +/- 0.03106576179376513
-211: 19.917257123997253 +/- 0.030237707990851084
321: 2.5091559778270263 +/- 0.00452871814381463
2212: 1.2080367749960197 +/- 0.0017990168407428205
-2212: 1.1841653771001384 +/- 0.0022883792488439113
310: 2.4771334163238206 +/- 0.005062715754942882
130: 2.478430561372695 +/- 0.005332616683884886
3122: 0.27660226960676876 +/- 0.001019263469390375
-3112: 0.14694775926357573 +/- 0.0005268675769813814
3112: 0.1489626041765302 +/- 0.0005466195371052817
-3312: 0.039004230324167555 +/- 0.0003818290262320663
-3322: 0.03895379778970718 +/- 0.0002810413157172156
-3222: 0.1478012322015245 +/- 0.0005077271022564136
3312: 0.0394429962610985 +/- 0.00026911867691313605
-3212: 0.15137462751771044 +/- 0.0007458148310844783
3212: 0.1530980795981008 +/- 0.000541970887712472
431: 0.011680591721752178 +/- 0.0001220635189581891
-431: 0.011736006928639369 +/- 0.0001577886845584461
3322: 0.03921649366644618 +/- 0.00017223818349375804
3334: 0.0011884125526735025 +/- 3.9537464581765634e-05
-531: 0.0009541402822744542 +/- 4.3581586794514795e-05
-3334: 0.0011535989893293526 +/- 4.818729437508582e-05
4232: 0.0005907387777848652 +/- 2.773825052736268e-05
-4232: 0.000587986707038012 +/- 2.8330240323640608e-05
531: 0.0009796135921167058 +/- 5.603069155408332e-05
-4132: 0.0005718122133368023 +/- 2.6362884241319027e-05
4132: 0.0005801503602583782 +/- 3.3810768997815116e-05
-5132: 4.406953136871157e-05 +/- 9.302429642479586e-06
5232: 5.356671200617856e-05 +/- 1.167617182010874e-05
5132: 6.0287886097844365e-05 +/- 1.6062209704276354e-05
-5232: 5.535451768517327e-05 +/- 1.1048594948426555e-05
-4332: 1.775848966145227e-05 +/- 7.200486425138621e-06
4332: 1.9997563119854696e-05 +/- 5.412373959099473e-06
-5332: 4.02247016793708e-06 +/- 1.7331716095700022e-06
-321: 2.5022140903735184 +/- 0.0038334664572049833
5332: 4.76368113571336e-06 +/- 2.0412534002839815e-06

Question 2:
The mutatated variants were denoted with a negative ID so to compare asymetry, the difference between ID vs -ID was calculated.
The calculation was done by making a list of mean differences across the 10 subsamples bewtween ID and -ID.
There are 2 ID's that did not have a negative counterpart (310 and 130), so these were not compared.
the standard deviation off the mean differences for each couple served as the uncertainty.
Significance was calculated by abs(x)/uncertainty.

Results:
3222 vs -3222: Significant within: 3.088 σ
211 vs -211: Significant within: 7.534 σ
321 vs -321: Significant within: 1.69 σ
2212 vs -2212: Significant within: 10.605 σ
3122 vs -3122: Significant within: 8.862 σ
3112 vs -3112: Significant within: 4.672 σ
3312 vs -3312: Significant within: 1.369 σ
3212 vs -3212: Significant within: 2.38 σ
431 vs -431: Significant within: 1.481 σ
3322 vs -3322: Significant within: 1.658 σ
3334 vs -3334: Significant within: 2.066 σ
4232 vs -4232: Significant within: 1.425 σ
531 vs -531: Significant within: 2.155 σ
4132 vs -4132: Significant within: 1.942 σ
5232 vs -5232: Significant within: 1.225 σ
5132 vs -5132: Significant within: 1.058 σ
4332 vs -4332: Significant within: 1.583 σ
5332 vs -5332: Significant within: 1.225 σ

Question 3:
For lower momenta the error bars are small and they increase generally with momentum. Most data points and their error bars are consistent with 0. This means that in general there was no significant asymmetry between the normal and mutant ID's. (For the plots see the other files in the github.)

