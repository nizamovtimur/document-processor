class DB:
    """Database interface"""

    def __init__(self):
        self.objects = {}

    def select(self, pk):
        """SELECT * FROM objects WHERE pk = @pk LIMIT 1

        Args:
            pk (object): primary key

        Returns:
            object: first object from query
        """
        if pk in self.objects:
            return self.objects[pk]
        return None

    def insert(self, obj):
        """INSERT INTO objects VALUES (...)

        Args:
            obj (object): object for insert
        """
        self.objects[obj.pk()] = obj

    def update(self, obj):
        """UPDATE objects SET ... WHERE pk = @pk

        Args:
            obj (object): object for update
        """
        self.insert(obj)
