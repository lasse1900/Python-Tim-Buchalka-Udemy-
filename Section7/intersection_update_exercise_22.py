text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.

splitted_text = text.split()
preps_used = prepositions.intersection(splitted_text)
print(preps_used)