# Classes Intro in Python

# 1. Encapsulation:
- Put together a list of attributes common in a class

# 2. Abstraction
- Certain functionalites which need not be given to the object (private functions)
- E.g. if you have an exam, all the student should know is that there is an evalutate method but you do not know how the method actually works. 
- Hence, abstraction dictates that you may not need to know the actual implementation of the method but just only the signature of the method.

#3. Inheritance
- Helps us extract the common functionalities/attributes further.
- E.g. we can make a class called school_members inside which we can have some common attributes among all members of the school such as age.
- Then the rest of the classes like student class, teacher class can inherit from the school_members class and then implement their own specific atrributes

#4. Polymorphism
- A given object can exist in multiple forms.
- For example, we have to create a list of questions for an exam. Each question can have different type, hence the same question is existing in different forms(e.g. mcq,long-answer,short-answer)
