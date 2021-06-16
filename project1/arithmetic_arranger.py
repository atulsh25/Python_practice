def arithmetic_arranger(problems,answer=True):
  var=answer
  if len(problems) > 5:
        return "Error: Too many problems."
  op = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y}

  list_for_first=list()
  list_for_oper=list()
  list_for_sec=list()
  list_for_under=list()
  list_for_res=list()
  for st in problems :
      new_str=st
      pos=new_str.find(" ")
      first_set=new_str[:pos]
      list_for_first.append(first_set)
      operator=new_str[pos+1:pos+2]
      list_for_oper.append(operator)
      second_set=new_str[pos+3:]
      list_for_sec.append(second_set)
      list_for_res.append(str(op[operator](int(first_set),int(second_set))))
  for i in range(len(list_for_first)):
    if not (list_for_first[i].isdigit() and list_for_sec[i].isdigit()):
      return "Error: Numbers must only contain digits."

  for i in range(len(list_for_first)):
    if len(list_for_first[i]) > 4 or len(list_for_sec[i]) > 4:
      return "Error: Numbers cannot be more than four digits."
  count=0
  for final_res in list_for_first:
    if len(final_res)<len(list_for_sec[count]):
      new_var=final_res.rjust(len(list_for_sec[count])-len(final_res)+2,' ')
      list_for_first[count]=new_var
      new_var1=list_for_oper[count]+(list_for_sec[count].rjust(len(list_for_sec[count])-len(final_res)+1,' '))
      list_for_sec[count]=new_var1
    else :
      new_var=" "*2 +final_res
      list_for_first[count]=new_var
      new_var1=list_for_oper[count]+" "+list_for_sec[count]
      list_for_sec[count]=new_var1
    list_for_under.append((len(list_for_res[count])+1)*"-")
    list_for_res[count]=" "+list_for_res[count]
    count=count+1

  if var:
    final1='    '.join(list_for_first)
    final2= '    '.join(list_for_sec)
    final3='    '.join(list_for_under)
    final4='    '.join(list_for_res)
    arranged_problems=final1+'\n'+final2+'\n'+final3
  else :
    final1='    '.join(list_for_first)
    final2= '    '.join(list_for_sec)
    final3='    '.join(list_for_under)
  final4='    '.join(list_for_res)
  arranged_problems=final1+'\n'+final2+'\n'+final3+'\n'+final4

  return arranged_problems