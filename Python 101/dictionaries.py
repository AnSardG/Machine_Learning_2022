"""
Dictionaries doesn't have a positional natural order, each value will be
directly linked to a String definition such as "Name" or "Age" or "Smokes"
this Strings will be named as "Keys", and the values can be any data type.
"""
patient = {
    "Name":"Juan",
    "Age":32,
    "Weight":70.5,
    "Smokes":False
}
print(patient)
# Easiest way to get a value from a key is like this.
print(patient["Name"])
# Another way is to use the get method.
print(patient.get("Age"))
"""
You can store a key from a dictionary and then the full registry
of that key will be eliminated this way (like lists).
"""
patientAge = patient.pop("Age")
print("Saved age:",patientAge)
print(patient)
#This method will add back again the key and value that you want.
patient.update({"Age":18})
print(patient)
patient.pop("Age")
print(patient)
# But also you can add the key directly without using the update method like this.
patient["Age"] = 19
print(patient)
# This will return a boolean, it's like questioning if the key is IN the dictionary.
print("Weight" in patient)
print("Weights" in patient)

patient2 = {"Name":"Pepe", "Age":23, "Weight":100.5, "Smokes":True}
patient3 = {"Name":"Antonio", "Age":19, "Weight":55.5, "Smokes":False}
# You can add dictionaries to a list, this is really powerful.
patients = [patient, patient2, patient3]
print(patients)
"""
In general dictionaries' keys are Strings but you can also use an  integer 
as the key;but of course it doesn't make much sense since lists are better
in this cases.
"""
football_players = {1:"Joseph",2:"Frederic",3:"Juan"}
print(football_players)

"""
Dictionaries aren't arrays (sucession of items) but you can manage them as 
so. This can be treated as a relational array (each item is linked to 
a key) "k" means Key and "v" means Value, this is a convention.

This for is basically a foreach using the method "items" that gives you
the view of the dictionary's items.

We also added a normal for to iterate all the patient dictionaries stored in the list "patients"
"""
for i in range(len(patients)):
    print("Patient number",i + 1, "\n")
    for k, v in patient.items():
        print("Key: " + k + ". Value:",v)
        if (k == "Age" and v <25):
            print("This patient is younger than 25 years old")
        print("------------------------")