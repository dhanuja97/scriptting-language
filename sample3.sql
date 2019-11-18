DECLARE
 a number;
 b number;
 c number;
 BEGIN
 a:=&a;
 b:=&b;
 c:=a+b;
 dbms_output.put_line(c);
 END;
 /
