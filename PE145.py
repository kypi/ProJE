import cProfile
import gc

# import re

rev_nums = []
non_rev = []
tested_nums = []
tested_nums2 = {}


rev_count = 0
odds = {1:1,3:3,5:5,7:7,9:9,'1':1,'3':3,'5':5,'7':7,'9':9};


a1 = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
a10 = {20:0,30:0,40:0,50:0,60:0,70:0,80:0,90:0}
a100 = {200:0,300:0,400:0,500:0,600:0,700:0,800:0,900:0}
a1000 = {2000:0,3000:0,4000:0,5000:0,6000:0,7000:0,8000:0,9000:0}
a10000 = {20000:0,30000:0,40000:0,50000:0,60000:0,70000:0,80000:0,90000:0}
a100000 = {200000:0,300000:0,400000:0,500000:0,600000:0,700000:0,800000:0,900000:0}
a1000000 = {2000000:0,3000000:0,4000000:0,5000000:0,6000000:0,7000000:0,8000000:0,9000000:0}
a10000000 = {20000000:0,30000000:0,40000000:0,50000000:0,60000000:0,70000000:0,80000000:0,90000000:0}
a100000000 = {200000000:0,300000000:0,400000000:0,500000000:0,600000000:0,700000000:0,800000000:0,900000000:0}
a1000000000 = {2000000000:0,3000000000:0,4000000000:0,5000000000:0,6000000000:0,7000000000:0,8000000000:0,9000000000:0}



def reverse2(n):
	digits = []
	tens = 1

	while(tens <= n):
		digits.insert(0,int(n/tens%10))
		tens*=10
	revn = 0
	tens=1
	for i in digits:
		revn+=i*tens
		tens*=10

	return revn

def reverse3(n):
	tens = 1
	revn = 0
	while(tens<=n):
		revn = revn*10 + int(n/tens%10)
		tens*=10
	return revn

# print(c)
def reverse(n):
	return int(str(n)[::-1])

def reverse_str(nstr):
	return int(nstr[::-1])

def digits_odd3(n):
	for character in str(n):
		if(character not in odds):
			return False
	return True

def digits_odd(n):
	for character in str(n):
		if(not int(character) % 2):
			return False
	return True

def digits_odd2(n):
	tens = 1
	while(tens <= n):
		if((int(n/tens%10)%2)<1):
			return False
		tens*=10
	return True

def is_reversable(n,revn):
	return digits_odd3(n+revn)

def testing():
	print("testing")

def check_testnums(n):
	return n in tested_nums2

def check_firstlast(nstr):
	if((nstr[-1] in odds) and (nstr[0] in odds)):
		return True
	elif((nstr[-1] not in odds) and (nstr[0] not in odds)):
		return True
	else: 
		return False


def revcount_to(maxnum):
	rev_count = 0
	for n in range(1,maxnum):
		if(n%10==0):
			continue
		# tested_nums.sort()
		if(check_testnums(n)):
			tested_nums2.pop(n,None)
			continue

		nstr = str(n)
		revn=reverse_str(nstr)

		# If first and last digit are both odds or both evens, then we know this is not reversible.
		if(check_firstlast(nstr)):
			tested_nums2[revn] = 0
			continue

		tested_nums2[revn] = 0
		# if(is_reversable(n,revn)):
		if(digits_odd3(n+revn)):
			rev_count+=1
	print(rev_count)
	return rev_count

def revcount_spaghetti(maxnum):
	rev_count = 0
	n = 1

	while(n<maxnum):
		if(True):
			pass

		elif(n>1000000000):	
			if n in a1000000000:
				multiple = n/1000000000
				n+=int(111111111*multiple)
		elif(n>100000000):	
			if n in a100000000:
				multiple = n/100000000
				n+=int(11111111*multiple)
		elif(n>10000000):	
			if n in a10000000:
				multiple = n/10000000
				n+=int(1111111*multiple)
		elif(n>1000000):	
			if n in a1000000:
				multiple = n/1000000
				n+=int(111111*multiple)
		elif(n>100000):	
			if n in a100000:
				multiple = n/100000
				n+=int(11111*multiple)
		elif(n<1000):	
			if n in a100:
				multiple = n/100
				n+=int(11*multiple)
		elif(n<10000):	
			if n in a1000:
				multiple = n/1000
				n+=int(111*multiple)
		elif(n<100000):	
			if n in a10000:
				multiple = n/10000
				n+=int(1111*multiple)
		
		
		
		
		


		if(n%10==0):
			n+=1
			continue
		# tested_nums.sort()
		if(n in tested_nums2):
			del tested_nums2[n]
			n+=1
			continue

		nstr = str(n)
		revn=int(nstr[::-1])

		# If first and last digit are both odds or both evens, then we know this is not reversible.
		if((nstr[-1] in odds) and (nstr[0] in odds)):
			tested_nums2[revn] = 0
			n+=1
			continue
		elif((nstr[-1] not in odds) and (nstr[0] not in odds)):
			tested_nums2[revn] = 0
			n+=1
			continue
		
		if(revn != n):
			tested_nums2[revn] = 0

		num = n+revn
		all_odd = True
		for char in str(num):
			if(char not in odds):
				all_odd = False
		if(all_odd):
			print(n)
			if(revn!=n):
				rev_count+=2
			else:
				rev_count+=1
			# rev_count+=1
		n+=1
	print(rev_count)
	return rev_count



def revcount_spaghetti2(maxnum):
	rev_count = 0
	n = 1
	print("testing")
	digits = [0,0,0,0,0,0,0,0,0]
	for d8 in range(0,10):
		digits[8] = d8
		print('d8 is ' + str(d8))
		boun = d8
		first_digit = 8
		for d7 in range(0,10):
			digits[7] = d7
			if(d8==0):
				boun = d7
				first_digit = 7
			for d6 in range(0,10):
				digits[6] = d6
				# print('d6 is ' +str(d6))
				if(d8==0 and d7==0):
					boun = d6
					first_digit = 6
				for d5 in range(0,10):
					digits[5] = d5
					if(d8==0 and d7==0 and d6==0):
						boun = d5
						first_digit = 5
					for d4 in range(0,10):
						digits[4] = d4
						if(d8==0 and d7==0 and d6==0 and d5==0):
							boun=d4
							first_digit = 4
						for d3 in range(0,10):
							digits[3] = d3
							if(d8==0 and d7==0 and d6==0 and d5==0 and d4==0):
								boun = d3
								first_digit = 3
							for d2 in range(0,10):
								digits[2] = d2
								if(d8==0 and d7==0 and d6==0 and d5==0 and d4==0 and d3==0):
									boun = d2
									first_digit = 2
								for d1 in range(0,10):
									digits[1] = d1
									if(d8+d7+d6+d5+d4+d3+d2==0):
									# if(d8==0 and d7==0 and d6==0 and d5==0 and d4==0 and d3==0 and d2==0):
										boun = 1
										first_digit = 1
									if(boun==0):
										boun = 1
									# TODO: make this even/odd based on the first digit (still keep bound)
									for d0 in range(boun,10):
										digits[0] = d0
										# print("N: " + str(n))
										# print("First digit: "+str(digits[first_digit]))
										n = int(1e8*d8+1e7*d7+1e6*d6+1e5*d5+1e4*d4+1e3*d3+1e2*d2+1e1*d1+d0)

										# if(first_digit>3):
										# 	if(d0 == digits[first_digit]):
										# 		if(d1 > digits[first_digit-1]):
										# 			continue
										# 		if(d2 > digits[first_digit-2]):
										# 			continue

										# print("This is n: "+ str(n))
										# if(n in tested_nums2):
										# 	# print("Skipping " + str(n))
										# 	del tested_nums2[n]
										# 	continue

										nstr = str(n)
										revn=int(nstr[::-1])
										if(revn<n):
											continue



										if((d0 in odds) and (digits[first_digit] in odds)):
											# if(revn != n):
											# 	tested_nums2[revn] = 0
											continue
										elif((d0 not in odds) and (digits[first_digit] not in odds)):
											# if(revn != n):
											# 	tested_nums2[revn] = 0
											continue

										# if(revn != n):
										# 	tested_nums2[revn] = 0
										num = n+revn
										all_odd = True
										for char in str(num):
											if(char not in odds):
												all_odd = False
										if(all_odd):
											if(revn!=n):
												rev_count +=2
											else:
												rev_count +=1
	print(rev_count)
	return rev_count

					

cProfile.run('revcount_spaghetti2(1000)')
# print(revcount_to(1000))



# if(True):
# 			pass
# 		elif(n>99999999):
# 			if(n%100000000==0):
# 				multiple = n/100000000
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(11111111*(multiple))
# 		elif(n>10000000):
# 			if(n%10000000==0):
# 				multiple = n/10000000
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(1111111*(multiple))
# 		elif(n>1000000):
# 			if(n%1000000==0):
# 				multiple = n/1000000
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(111111*(multiple))
# 		elif(n>100000):
# 			if(n%100000==0):
# 				multiple = n/100000
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(11111*(multiple))
# 		elif(n>10000):
# 			if(n%10000==0):
# 				multiple = n/10000
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(1111*(multiple))
# 		elif(n>1000):
# 			if(n%1000==0):
# 				multiple = n/1000
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(111*(multiple))
# 		elif(n>100):
# 			if(n%100==0):
# 				multiple = n/100
# 				if(n==1):
# 					continue
# 				else:
# 					n+=int(11*(multiple))