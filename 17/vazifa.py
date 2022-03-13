class User:
  def __init__(self, first_name, last_name, age, email, phone, lang):
    self.fist_name=first_name
    self.last_name=last_name
    self.age=age
    self.email=email
    self.phone=phone
    self.lang=lang
  
  def get_full_name(self):
    return f"{self.fist_name} {self.last_name}"

user1 = User("Hasan", "Husanov", 20, "example@gmail.com", "+123456789", "uz")
print(user1.get_full_name())