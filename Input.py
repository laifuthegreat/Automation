from URLtools import garnish_url
import winsound

def put_in(results):
	i = 1
	for result in results:
		print(str(i)+" "+result)
		i+=1
	print(str(i)+" Manual Input:")
	print(str(i+1)+" None")
	winsound.Beep(1000,500)
	response = input()
	if response == str(i):
		winsound.Beep(1000,500)
		print("URL:", " ", end="")
		return garnish_url(input())
	elif response == str(i+1):
		return None
	else:
		return results[int(response)-1]

def put_in_pair(results):
	i = 1
	for result in results:
		print(str(i)+" "+str(result))
		i+=1
	print(str(i)+" Manual Input:")
	print(str(i+1)+" None")
	winsound.Beep(1000,500)
	response = input()
	if response == str(i):
		winsound.Beep(1000,500)
		print("URL:", " ", end="")
		return garnish_url(input())
	elif response == str(i+1):
		return None
	else:
		return results[int(response)-1].get_second()