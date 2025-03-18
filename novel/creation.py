from Characters import Male_Characters,Female_Characters
from God_Relam import divine_Region

male_character_1=Male_Characters("yun che",42,"Good","Male")
female_character_1=Female_Characters("Qianye Yinger",1010,"Good","Female")

Region_1=divine_Region("Southern Divine Region",2,"Normal Profound Energy")


print(male_character_1.name)
print(female_character_1.name)
print(Region_1.name + " is the most powerful in God Relam")
print(male_character_1.Villain_or_Hero())
print(male_character_1.power_Inheritance())

