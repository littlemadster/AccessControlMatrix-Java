'''
ACM CLASS


    ### UPDATE TO MAKE LABELS AN OBJECT THAT CAN BE MANIPULATED/CHANGED ###
    
'''


from tkinter import *
from tkinter import ttk
import operator

class LabelACM:

    def __init__(self, name, text, row, column):
        self.name = name
        self.text = text
        self.row = row
        self.column = column
        self.rights = []
        
        

class ACM:

    subjects = [] #list of subjects that are created
    objects = [] #list  of objects that are created
    rights = [] #list of rights that are created
    counter =0
    

    def createObj(objName):  #takes window and object name to create new object onto window
        ''' CHECK IF OBJECT ALREADY EXISTS'''
        newObject = LabelACM(objName, objName, 0, len(ACM.objects)+1)
        ACM.objects.append(newObject) #add object to object list
        
    def createSub(subName): #takes window and subject name to create new subject onto window
        ''' CHECK IF SUBJECT ALREADY EXISTS'''
        newSubject = LabelACM(subName, subName, len(ACM.subjects)+1, 0)
        ACM.subjects.append(newSubject) #add object to object list
        ACM.createObj(subName)
                

    def initRules():

        for i in range(len(ACM.subjects)):
            for j in range(len(ACM.objects)):
                newRight = LabelACM(ACM.subjects[i].name + ACM.objects[j].name, ACM.subjects[i].name + ACM.objects[j].name, ACM.subjects[i].row, ACM.objects[j].column)
                ACM.rights.append(newRight)
               # print(newRight.name + ": " + str(newRight.row) + " " + str(newRight.column)) 
        
    def grant(subName, objName, right): #grants subject right to object based on subject, object, and desired right

        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subName:
                subI = ACM.subjects[i].name
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objName:
                objI = ACM.objects[j].name
                break
   
        for k in range(len(ACM.rights)): #searches for right location within rights list
            if ACM.rights[k].name == subI + objI: #if name is found
                if right not in ACM.rights[k].rights: #if right does not already exist
                    ACM.rights[k].rights.append(right) #add right
                    #print("rights: " +  ACM.rights[k].text + " " + str(ACM.rights[k].rights))
                    break
            
                        
    def removeRight(subName, objName, right):
        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subName:
                subI = ACM.subjects[i].name
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objName:
                objI = ACM.objects[j].name
                break

        for k in range(len(ACM.rights)): #searches for right location within rights list
            if ACM.rights[k].name == subI + objI: #if name is found
                if right in ACM.rights[k].rights: #if right does not already exist
                    ACM.rights[k].rights.remove(right) #add right
                    #print("rights: " +  ACM.rights[k].text + " " + str(ACM.rights[k].rights))
                    break


    def transfer(subNameF, objNameF, right, subNameT, objNameT, rightT): #subject from, object from, right, subject to, object to
        possible = 0
        
        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subNameF:
                subF = ACM.subjects[i].name
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objNameF:
                objF = ACM.objects[j].name
                break

        for i in range(len(ACM.subjects)): #finds name of subject
            if ACM.subjects[i].name == subNameT:
                subT = ACM.subjects[i].name
                break

        for j in range(len(ACM.objects)): #finds name of object
            if ACM.objects[j].name ==  objNameT:
                objT = ACM.objects[j].name
                break
        
        for k in range(len(ACM.rights)): #searches for right location within rights list
            if ACM.rights[k].name == subF + objF: #if name is found
                if right in ACM.rights[k].rights and operator.contains(right, "*"): #if right does exist
                    possible = 1

        if possible == 1:
            for k in range(len(ACM.rights)):
                if ACM.rights[k].name == subT + objT: #if name is found
                    if rightT not in ACM.rights[k].rights: #if right does not already exist
                        ACM.rights[k].rights.append(rightT) #add right
                        print("rights: " +  ACM.rights[k].text + " " + str(ACM.rights[k].rights))
                        break

    def read(): #prints all rights for subjects and objects
        print("Rights are defined as 'subject name' concatinated with 'object name' and printed with their rights.")
        for i in range(len(ACM.rights)):
            print(ACM.rights[i].text + " " + str(ACM.rights[i].rights))
   
    def delRecursive(name): #checks if that subject, or object exist and deletes it 
        for m in range(len(ACM.rights)):
            if name in ACM.rights[m].text: #if objname matches name in array 
                print("Name:--> ",str(ACM.rights[m].text))   
                del ACM.rights[m]   #delete rights
                ACM.delRecursive(name)
                break
        
    def delObj(objName): #delete object from ACM
        for i in range(len(ACM.rights)):
            if objName in ACM.rights[i].text: #objname exist in array 
                ACM.delRecursive(objName) #find any place that has this object name and delete it
                break                      
        
        # delets the object in the array  
        for i in range(len(ACM.objects)):
             if ACM.objects[i].text ==  objName: #if objname matches name in array 
                 del ACM.objects[i] #delete object column
                 break


    def deSub(subName):     
        for i in range(len(ACM.rights)):
            print( ACM.rights[i].text)
            if subName in ACM.rights[i].text: #if objname matches name in array 
                ACM.delRecursive(subName)
                del ACM.objects[i]  #deletes subject from column

                break                      
        
        #  objects array 
        for k in range(len(ACM.subjects)):
             if ACM.subjects[k].text ==  subName: #if objname matches name in array 
                 del ACM.subjects[k]    #deletes subject from object
                 break
    
    
        
def main():
     
    def close():
        window.destroy()

    window = Tk()
    window.title("ACM")
    window.geometry('900x400')

    Button(window, text="Quit", command=close).grid(row=0, column=0)
    ACM.createObj("Obj1")
    ACM.createObj("Obj2")
    ACM.createObj("Obj3")
    ACM.createObj("Obj4")
    ACM.createSub("Sub1")
    ACM.createSub("Sub2")
    ACM.createSub("Sub3")
    ACM.createSub("Sub4")




    
    #ACM.delObj(window, "Obj1")
    ACM.initRules()

    ACM.grant("Sub1", "Obj1", "read")
    ACM.grant("Sub1", "Obj1", "write")
  
    ACM.grant("Sub2", "Obj2", "write")
    ACM.grant("Sub2", "Obj2", "control")
    ACM.grant("Sub2", "Obj1", "write")


    ACM.grant("Sub3", "Sub1", "view")
    ACM.grant("Sub4", "Sub2", "control")


    #ACM.removeRight("Sub1", "Obj1", "control")
    #ACM.removeRight("Sub1", "Obj1", "own")
    #ACM.removeRight("Sub3", "Obj4", "read")

    #ACM.transfer("Sub3", "Obj4", "read*", "Sub1", "Obj2", "read")
    #ACM.delObj("Obj1")
    #ACM.deSub("Sub3")

    

    #ACM.read()


    for i in range(len(ACM.objects)):
        printObj = Label(window, text = ACM.objects[i].text)
        printObj.grid(row = ACM.objects[i].row, column = ACM.objects[i].column)

    for i in range(len(ACM.subjects)):
        printSub = Label(window, text = ACM.subjects[i].text)
        printSub.grid(row = ACM.subjects[i].row, column = ACM.subjects[i].column)
        
    for i in range(len(ACM.rights)):
        #print("\nPrinting: "+ACM.rights[i].text + " " + str(ACM.rights[i].rights))
        printRight = Label(window, text = ACM.rights[i].rights)
        printRight.grid(row = ACM.rights[i].row, column = ACM.rights[i].column)

        
    #ACM.delRight(window, "Sub1", "Obj1", "control")
    #ACM.delRight(window, "Sub1", "Obj1", "write")
    #ACM.delRight(window, "Sub3", "Obj4", "read")'''
    

    window.mainloop()

main()

