# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys

# KEY can be integer, float, boolean, tuple

info = {
    "key": "value",
    "name": "codex",
    "age": 23,
    "Friends": ["arun","varun","sahrun"],
    "learning": "python",
    "is_adult": True
}
null_dict = {} # NOT A SINGLE VALUE

null_dict["name"] = "NULLYFI" # ONE VALUE ADDED TO IT

info["name"] = "CodeY" # overwrite key's value
info["surname"]= "CodeZ" # new key value pair added

print(info)
print(null_dict)

# NESTED DICTIONARY 
student = {
    "name" : "Ram",
    "score": {
        "chemistry" : 90,
        "physics" : 90,
        "maths" : 95
    }

}
print(student)
print(student["score"])

# DICTIONARY METHODS
print(student.keys()) #return all keys
print(student.values()) # return all values
print(student.items()) # return all (key,val)pairs as tuples
print(student.get("name")) # get("key") return value associated with the key

print( list(student.keys())) # TYPECASTING DICTIONARY TO LIST

print(student["name2"]) # key not present so show error
print(student.get("name2")) # key not presetn but print NONE

student.update(info) # info divtionary added to the student dictionary
print(student)


# ------------------- SET -------------------
# Set is the collection of the unordered items. 
# Each element in the set must be unique & immutable. SET IS MUTTABLE (WE CAN ADD AND REMOVE VALUES FROM IT)
collection = {1,2,2,3, "heelo", "heelo", 4} # duplicate value get ignored
print(collection)
print(type(collection))


collection1 = {} # ITS EMPTY DICTIONARY
collection1 = set() # ITS EMPTY SET
collection1.add(1)
collection1.add(2)
collection1.add(2)
print(collection1)
collection1.remove(1) # remove(value) if value not present then ERROR 
print(collection1)

# collection1.clear() 
# print(collection1)

print(collection1.pop()) # RANDOMLY POP (REMOVE) ELEMENT AND PRINT 


set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) # SIMPLE UNION OPERARION AND RETURN NEW SET DO NOT ALTER THE ORIGINAL SET
print(set1.intersection(set2))# SIMPLE INTERSECTION OPERARION AND RETURN NEW SET DO NOT ALTER THE ORIGINAL SET


word_meaning = {
    "table" : ["a piece of furniture", "list of facts"],
    "cat" : "a samll animal"

}

sub = {"python" , "java", "C++","python","javascript","java","python","java","C++","C"}
print(len(sub))


marks = {}
x = int(input("enter physics marks"))
marks.update({"phy":x})

y = int(input("enter ch marks"))
marks.update({"ch":y})

z = int(input("enter ma marks"))
marks.update({"ma":z})

print(marks)

set = {("float" , 9.0) , ("int", 9)}
print(set)