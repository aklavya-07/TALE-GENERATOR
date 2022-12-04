import random
li_story = ["A woman finds a pot of treasure on the road while she is returning from work.Delighted (very happy) with her luck, she decides to keep it. As she is taking it home, it keeps changing.However, her enthusiasm refuses to fade away (disappear or faint slowly).What Is Great About It: The old lady in this story is one of the most cheerful characters anyone can encounter in English fiction.Her positive disposition (personality) tries to make every negative situation seem like a gift, and she helps us look at luck as a matter of our view rather than events.",
            "This classic fable (story) tells the story of a very slow tortoise (turtle) and a speedy hare (rabbit).The tortoise challenges the hare to a race. The hare laughs at the idea that a tortoise could run faster than he, but the race leads to surprising results.What Is Great About It: Have you ever heard the English expression, “Slow and steady wins the race”? This story is the basis for that common phrase.This timeless (classic) short story teaches a lesson that we all know but can sometimes forget: Natural talent is no substitute for hard work, and overconfidence often leads to failure."
            , "Timmie Willie is a country mouse who is accidentally taken to a city in a vegetable basket. When he wakes up, he finds himself at a party and makes a friend.When he is unable to bear (tolerate or experience) the city life, he returns to his home but invites his friend to the village.", "When his friend visits him, something similar happens.What Is Great About It: Humans have been living without cities or villages for most of history.That means that both village and city life are recent inventions. And just like every other invention, we need to decide their costs and benefits.The story is precisely (exactly) about this debate. It is divided into short paragraphs and has illustrations for each scene. This is best for beginners who want to start reading immediately."]

li_heading = ["“The Bogey Beast” by Flora Annie Steel",
              "“The Tortoise and the Hare” by Aesop", 
              "“The Tale of Johnny Town-Mouse” by Beatrix Potter"]
while True:
    r = random.randint(0, 2)
    print(li_heading[r])
    print(li_story[r])
    print("want new story", "1-->yes", "0-->no exit")
    a = int(input())
    if a == 1:
        continue
    else:
        break
GHGH
