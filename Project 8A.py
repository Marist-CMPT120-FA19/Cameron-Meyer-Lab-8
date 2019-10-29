def average(avg):
  if int(avg)<60 or avg>80:
    return  True
  else:
    return False
  
 
def line():
  print(50*"=")


def degreeDays(avg):
  cooling = 0
  heating = 0
  for i in range(len(avg)):
      if avg[i]>80:
        heating = heating +(avg[i]-80)
      if avg[i]<60:
        cooling = cooling + (60-avg[i])
        
  return cooling , heating

  
def intro():
    print("Enter the daily temperature to determine the number of heating or cooling days.")

def stlist(avg):
  avgtlist = []
  for num in avg.split():
    num = int(num)
    avgtlist.append(num)
  avg = avgtlist
  return avg


def main():
  
  intro()
  
  avg = input("Enter temperature: ")
  line()
  
  avg = stlist(avg)
  
  cooling, heating = degreeDays(avg)
  
  print("{0} {1}".format("Cooling Degree Days: ", heating))
  print("{0} {1}".format("Heating Degree Days: ", cooling))
  line() 

main()
