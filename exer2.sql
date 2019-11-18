declare
	CURSOR emp_cur is select ssn,name,salary from emp;
	emp_rec emp_cur%rowtype;
begin
	OPEN emp_cur;
	LOOP
	  FETCH emp_cur into emp_rec;
	  EXIT when emp_cur%notfound;
	  dbms_output.put_line(emp_rec.ssn||''||emp_rec.name);
	END LOOP;
	close emp_cur;
END;
/	 	
