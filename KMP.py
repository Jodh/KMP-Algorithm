# processes the given pattern to create a partial match lookup table 
def createTempArray(P):
	'''Input: Pattern string, 
		Output : lookup table of length equal to the 
		pattern length'''
	i,j = 1,0
	TempArray = [0]
	while i < len(P):
		if P[j] == P[i]:
			TempArray.append(j+1)
			j += 1
			i += 1
		elif j == 0:
			TempArray.append(0)
			i += 1
		else:
			j = TempArray[j-1]
			
	return TempArray 

P = raw_input("enter pattern string: ")
TempArray = createTempArray(P)
print TempArray

# compaires the pattern P and text T and prints out positions where matches occur
def KMP(T, P, TA):
	'''Input: Text string, Pattern String , Lookup table
		Output: All positions 
		where matches occur in the text, empty if no matches occur'''
	start,end = 0,0
	matchArray = []
	while end < len(T):
		#print "start =", start, "\nend =",end, "\n************"
		if start == len(P)-1 and P[start] == T[end]:
			#print "match found at ", end-len(P)+1
			matchArray.append(end-len(P)+1)
			start = 0
			continue
		elif P[start] == T[end]:
			start += 1
			end += 1
			continue
		elif start == 0 and P[start] != T[end]:
			#print "mis-match at ", start, "th position in the pattern"
			end += 1
			continue
		else:
			#print "mis-match at ", start, "th position in the pattern"
			start = TA[start-1]
	return matchArray

T = raw_input("enter Text string: ")
matchArray = KMP(T,P,TempArray)
print matchArray	

	
				
	

	
