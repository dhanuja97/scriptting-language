declare
t number;
fact1 number;

PROCEDURE procedure_fact(n in number,fact out number) is
i number;

BEGIN
	fact:=1;
	for i in 1..n loop
	
		fact:=fact*i;
	end loop;
end;

begin
t:=&t;
procedure_fact(t,fact1);
dbms_output.put_line('Answer is: '||fact1);
end;
/		
