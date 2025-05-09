from orm import BaseORMEntity, ManyToMany, Integer, String, EntityGenerator


class User(BaseORMEntity):
    id: Integer = Integer(nullable=False, pk=True)
    name: String = String(nullable=False)
    friends: ManyToMany = ManyToMany(mapped_entity=BaseORMEntity, mapped_attribute="friends", nullable=True)

User.friends = ManyToMany(mapped_entity=User, mapped_attribute="friends", nullable=True)

u = User()
gen = EntityGenerator()
s = gen.generate_schema(User)
print(s)