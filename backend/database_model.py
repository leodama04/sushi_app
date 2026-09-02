from sqlmodel import Field, SQLModel

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=120, index=True)
    description: str | None = None
    price: float = Field(gt=0)
