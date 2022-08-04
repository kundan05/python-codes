fine=0
reward=0
print("what is incredia")
print("a.student club")
print("b.college fest")
print("c.place")
print("d.block name")
ans1=input()
if (ans1=="b"):
    reward=reward+50
    print("correct answer your balance is", str(reward))
else:
    fine=fine+1
    print("wrong answer your balance is", str(reward))

    print("related to cornshop")
print("a.samosa")
print("b.juice")
print("c.corn")
print("d.all of the above")
ans2=input()
if (ans2=="d"):
    reward=reward+50
    print("correct answer your balance is" ,str(reward))
else:
    fine=fine+1
    print("wrong answer your balance is", str(reward))
    if (fine==2):
        print("pay the fine")

