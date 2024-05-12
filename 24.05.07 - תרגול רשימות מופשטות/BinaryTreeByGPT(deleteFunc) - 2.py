def delete(self, data):
    parent = None
    current = self.root

    # חיפוש צומת המכיל את הערך למחיקה
    while current and current.data != data:
        parent = current
        if data < current.data:
            current = current.left
        else:
            current = current.right

    # אם הערך לא נמצא
    if current is None:
        return

    # מחיקת הערך
    # אם הצומת המכיל את הערך ריקה
    if current.left is None and current.right is None:
        if parent:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
        else:
            self.root = None

    # אם הצומת המכיל את הערך יש בנים אחד או אף אחד
    elif current.left is None:
        if parent:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
        else:
            self.root = current.right
    elif current.right is None:
        if parent:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            self.root = current.left

    # אם הצומת המכיל את הערך יש בניים שניים
    else:
        successor_parent = current
        successor = current.right
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # העתקת הערך של המחליף למקום הצומת שנמחק
        current.data = successor.data

        # מחיקת הערך של המחליף מהעץ
        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right
