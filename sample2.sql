DECLARE
	a integer:=10;
	b integer:=20;
	c integer;
	f real;
BEGIN
	c:= a+b;
	dbms_output.put_line('value of c:'|| c);
	f:=70.0/3.0;
	dbms_output.put_line('value of f:'|| f);
END;
/		
