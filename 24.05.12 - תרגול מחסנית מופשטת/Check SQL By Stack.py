import StackClassUsingLinkedList
def check_SQL(SQL_code: list) -> bool:
    begin_and_end_st = StackClassUsingLinkedList.Stack()

    for i in SQL_code:
        if i == "BEGIN":
            begin_and_end_st.push(1)
        elif i == "END;":
            if begin_and_end_st.peek():
                begin_and_end_st.pop()
            else:
                return False
    if begin_and_end_st.peek():
        return False
    else:
        return True

SQL_code = """
DECLARE @MyVar INT;
BEGIN
SET @MyVar = 1;
WHILE @MyVar <= 10
BEGIN
PRINT @MyVar;
SET @MyVar = @MyVar + 1;
END;
END;
"""

print(check_SQL(SQL_code.split()))