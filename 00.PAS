program calc;
var a,b,c:integer;
d:string;
e:char;
begin;
writeln('write number A');
readln(a);
writeln('write operation + - * /');
readln(d);
writeln('write number B');
readln(c);
if d=('+') then b:=a+c;
if d=('-') then b:= a - c;
if d=('*') then b:=a*c;
if d=('/') then b:=a div c;
writeln('answer:',b);
readln;
write('do you want to use calculator again (Y/N): ');
readln(e);

if (e = 'Y') or (e = 'y') then
writeln('you have chosen to try again');
else
writeln('thanks');
end.