def arithmetic_arranger(problems, secondinput=False):

  problemarray = []
  lens = []
  result = []
  dash = ["--", "---", "----", "-----", "------"]
  width = []
  specialdash = []
  print(type(problems[0]), len(problems), problems[0].split(' ')[1])
  if len(problems) > 5:
    return "Error: Too many problems."

  for i in range(len(problems)):
    #print(i,"loophi",problems[i].split(' ')[1])
    if problems[i].split(' ')[1] != "+" and problems[i].split(' ')[1] != "-":
      return "Error: Operator must be '+' or '-'."

  for i in range(len(problems)):
    if problems[i].split(' ')[0].isdigit() != True or problems[i].split(
        ' ')[2].isdigit() != True:

      return "Error: Numbers must only contain digits."

  for i in range(len(problems)):
    if len(problems[i].split(' ')[0]) > 4 or len(
        problems[i].split(' ')[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

  for i in range(len(problems)):

    problemarray.append(problems[i].split(' '))
    width.append(
      len(str(max(int(problemarray[i][0]), int(problemarray[i][2])))))
    specialdash.append((dash[width[i]]))

  if secondinput == True:
    for i in range(len(problems)):
      if problemarray[i][1] == "+":
        result.append(str(int(problemarray[i][0]) + int(problemarray[i][2])))
      else:
        result.append(str(int(problemarray[i][0]) - int(problemarray[i][2])))

  space = " " * 4
  firstline = ""
  secondline = ""
  thirdline = ""
  dasher = ""
  dashresult = ""

  for i in range(len(problems)):

    if i != 0:
      firstline += space + " " + " " + problemarray[i][0].rjust(width[i])
    else:
      firstline += " " + " " + problemarray[i][0].rjust(width[i])
    if i != 0:
      secondline += space + problemarray[i][1] + " " + problemarray[i][
        2].rjust(width[i])
    else:
      secondline += problemarray[i][1] + " " + problemarray[i][2].rjust(
        width[i])
    if i != 0:
      dashresult += space + specialdash[i]
    else:
      dashresult += specialdash[i]
    if secondinput == True:
      if i != 0:
        thirdline += space + " " * (2 + width[i] - len(result[i])) + result[i]
      else:
        thirdline += " " * (2 + width[i] - len(result[i])) + result[i]

  output = firstline + "\n" + secondline + "\n" + dashresult
  if secondinput == True:
    output += "\n" + thirdline
    print("hello")

  print(output)

  arranged_problems = output
  return arranged_problems
