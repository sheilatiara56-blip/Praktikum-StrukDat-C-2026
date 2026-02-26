
ukm_coding = {"andi", "budi", "caca", "deni"}
ukm_robotik = {"caca","deni","elis","fafa"}

set1 =ukm_coding.difference(ukm_robotik)
print(set1)

set2 = ukm_robotik.union(ukm_coding)
print(set2)

isMember = "andi" in ukm_coding
print(isMember)