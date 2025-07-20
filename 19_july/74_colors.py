#Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and
# an end number between 5 and 9. Display the list for those colours between
# the start and end numbers the user input.

def colors(lst,start,end):

    return lst[start:end+1]



lst =['red','blue','green','white','yellow','magenta','cyan','violet','purple','pink']
start = int(input('enter start index 0-4: '))
end = int(input('enter end index 5-9: '))
print(colors(lst,start,end))