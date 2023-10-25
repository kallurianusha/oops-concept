# def addition(num1,num2):
#     print("addition=",num1+num2)
# def subtraction(num1,num2):
#     print("subtraction=",num1-num2)
# def multiplication(num1,num2):
#     print("multiplication=",num1*num2)
# def division(num1,num2):
#     print("division=",num1/num2)
# while True:
#     print("1. addition")
#     print("2. subtraction")
#     print("3. multiplication")
#     print("4. division")
#     print("5. exit")
#     choice=int(input("Enter your choice (1-5) : "))
#     if choice==1:
#         num1=int(input("Enter first number : "))
#         num2=int(input("Enter second number : "))
#         addition(num1,num2)
#     elif choice==2:
#         num1=int(input("Enter first number : "))
#         num2=int(input("Enter second number : "))
#         subtraction(num1,num2)
#     elif choice==3:
#         num1=int(input("Enter first number : "))
#         num2=int(input("Enter second number : "))
#         multiplication(num1,num2)
#     elif choice==4:
#         num1=int(input("Enter the first number : "))
#         num2=int(input("Enter the second number : "))
#         if num2 == 0:
#             print("infinity")
#         else:
#             division(num1,num2)
#     elif choice==5:
#         break
#     else:
#         print("Invalid input! Please enter a valid option.")



# class shoppingcart:
#     def __init__(self):
#         self.items = []
#     def add_item(self, item_name,quantity):
#         if item_name in self.items:
#             self.items[item_name]+=quantity
#         else:
#             self.items[item_name] = quantity
#     def remove_item(self, item_name,quantity):
#         if item_name in self.items:
#             if self.items[item_name]>=quantity:
#                 self.items[item_name] -= quantity
#                 if self.items[item_name]== 0:
#                    del self.items[item_name]
#             else: 
#                 print ("Not enough items to remove")
#         else:
#             print ("Item not found in cart")
#     def display_cart(self):
#         print("shopping cart:")
#         for item, quantity in self.items.items():
#             print(f"{item}:{quantity}")
# cart = shoppingcart()
# cart.add_item("apple",7)
# cart.add_item("kiwi",5)
# cart.add_item("banana",6)
# cart.display_cart()
# cart.remove_item("apple",2)
# cart.display_cart()


# patients = []
# def add_patient():
#     patient_id = input("Enter Patient ID: ")
#     name = input("Enter Name: ")
#     age = input("Enter Age: ")
#     gender = input("Enter Gender: ")
    
#     patient = {
#         "ID": patient_id,
#         "Name": name,
#         "Age": age,
#         "Gender": gender
#     }
    
#     patients.append(patient)
#     print("Patient added successfully!")
# def display_patients():
#     if not patients:
#         print("No patients in the system.")
#     else:
#         for patient in patients:
#             print("ID:", patient["ID"])
#             print("Name:", patient["Name"])
#             print("Age:", patient["Age"])
#             print("Gender:", patient["Gender"])
#             print("\n")
# def search_patient_by_id(patient_id):
#     for patient in patients:
#         if patient["ID"] == patient_id:
#             print("Patient found:")
#             print("ID:", patient["ID"])
#             print("Name:", patient["Name"])
#             print("Age:", patient["Age"])
#             print("Gender:", patient["Gender"])
#             return
#     print("Patient with ID", patient_id, "not found.")
# def delete_patient_by_id(patient_id):
#     for patient in patients:
#         if patient["ID"] == patient_id:
#             patients.remove(patient)
#             print("Patient with ID", patient_id, "deleted successfully.")
#             return
#     print("Patient with ID", patient_id, "not found.")
# def update_patient_by_id(patient_id):
#     for patient in patients:
#         if patient["ID"] == patient_id:
#             name = input("Enter new Name: ")
#             age = input("Enter new Age: ")
#             gender = input("Enter new Gender: ")
#             patient["Name"] = name
#             patient["Age"] = age
#             patient["Gender"] = gender
#             print("Patient with ID", patient_id, "updated successfully.")
#             return
#     print("Patient with ID", patient_id, "not found.")
# while True:
#     print("\nHospital Management System")
#     print("1. Add Patient")
#     print("2. Display Patients")
#     print("3. Search Patient by ID")
#     print("4. Delete Patient by ID")
#     print("5. Update Patient by ID")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_patient()
#     elif choice == "2":
#         display_patients()
#     elif choice == "3":
#         patient_id = input("Enter Patient ID to search: ")
#         search_patient_by_id(patient_id)
#     elif choice == "4":
#         patient_id = input("Enter Patient ID to delete: ")
#         delete_patient_by_id(patient_id)
#     elif choice == "5":
#         patient_id = input("Enter Patient ID to update: ")
#         update_patient_by_id(patient_id)
#     elif choice == "6":
#         print("Exiting the system. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")      