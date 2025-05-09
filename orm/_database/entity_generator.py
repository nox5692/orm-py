from .._entity import BaseORMEntity, Attribute, ManyToMany


class EntityGenerator:
    def generate_schema(self, e: BaseORMEntity) -> str:
        table_name: str = e.__class__.__name__.lower()
        out: str = f"CREATE TABLE {table_name}(\n"
        attrs: dict[str, Attribute] = e.get_descriptors()
        for name in attrs:
            out += f"\t{name} {attrs[name]._sql_type} {"NOT NULL" if not attrs[name]._nullable else ""},\n"
            if isinstance(attrs[name], ManyToMany):
                out += f"\tFOREIGN KEY({name}) REFERENCES {table_name}({attrs[name]._entity.id._name}),\n"
        out += ");"
        return out
