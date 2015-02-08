BOWL_INDEX = 6
pitSet = [5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5]
moveSet = []

def movePit(n, moveArr):
	numBeads = pitSet[n % len(pitSet)]
	lastPit = n + numBeads
	pitSet[n % len(pitSet)] = 0
	for i in range(n + 1, lastPit + 1):
		pitSet[i % len(pitSet)] += 1
	
	if len(moveArr) == 0:
		moveArr.append(n)
	
	moveArr.append(numBeads);
	if lastPit % len(pitSet) != BOWL_INDEX and pitSet[lastPit % len(pitSet)] > 1:
		movePit(lastPit, moveArr)
	else:
		moveSet.append(moveArr)

def undoMove():
	lastPit = moveSet[-1][0]
	for n in moveSet[-1][1:]:
		lastPit += n
	
	for n in reversed(moveSet[-1][1:]):
		for i in xrange(lastPit, lastPit - n, -1):
			pitSet[i % len(pitSet)] -= 1
		lastPit -= n
		pitSet[lastPit % len(pitSet)] = n
		
	pitSet[moveSet[-1][0]] = moveSet[-1][1]
	del moveSet[-1]
	
def testChain():
	found = False
	
	for i in range(0, BOWL_INDEX):
		if pitSet[i] == 0:
			continue
		
		movePit(i, [])
		
		lastPit = moveSet[-1][0]
		for n in moveSet[-1][1:]:
			lastPit += n
		lastPit %= len(pitSet)
		
		oppPit = len(pitSet) - lastPit - 1
		bonus = [0, 0]
		if lastPit == BOWL_INDEX:
			found = testChain()
		elif lastPit < BOWL_INDEX and pitSet[lastPit] == 1:
			bonus = [pitSet[lastPit], pitSet[oppPit]]
			pitSet[BOWL_INDEX] += bonus[0] + bonus[1]
			pitSet[oppPit] = 0
			pitSet[lastPit] = 0
		
		if found or pitSet[BOWL_INDEX] >= 31:
			found = True
			break
		else:
			pitSet[BOWL_INDEX] -= bonus[0] + bonus[1]
			pitSet[lastPit] += bonus[0]
			pitSet[oppPit] += bonus[1]
			undoMove()
	
	return found
	
def main():
	found = testChain()
	choices = []
	for m in moveSet:
		choices.append(m[0])
		
	print choices

if __name__ == "__main__":
	main()