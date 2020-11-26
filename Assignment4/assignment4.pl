domains
    name,address = symbol
    phone = string
    l = integer*
    
predicates
    start
    repeat
    selectItem(integer)
    studentData
    subjectL(l)
    searchByName(name)
    searchByPhone(phone)
database
    studentDB(name,address,phone,l)
goal
    clearwindow,
    makewindow(1,7,7,"Search Student Detail",0,0,25,80),
    start.
clauses
    repeat.
        repeat:-
            repeat.
    start:-
        repeat,
        write("\n0.Exit"),
        write("\n1.Enter student data"),
        write("\n2.Search by Name"),
        write("\n3.Search by Phone number"),
        write("\n4.Show all Student Data"),
        write("\nEnter your choice::"),
        readint(Choice),
        selectItem(Choice),
        Choice=0.
    selectItem(0).
    selectItem(1):-
        studentData,
        fail.
    selectItem(2):-
        write("\nEnter your name::"),
        readln(Name),
        searchByName(Name),
        fail.
    selectItem(3):-
        write("\nEnter the phone no::"),
        readln(Phone),
        searchByPhone(Phone),
        fail.
    selectItem(4):-
        studentDB(Name,Address,Phone,Marks),
        write(Name,"  ",Address,"  ",Phone,"  ",Marks),nl,
        fail.
    studentData:-
        write("\nEnter the name of the student::"),
        readln(Name),
        write("\nEnter the address of the student::"),
        readln(Address),
        write("\nEnter the phone number of the student::"),
        readln(Phone),
        write("\nEnter the five subject marks of the student"),
        subjectL(Marks),
        assert(studentDB(Name,Address,Phone,Marks)).
    subjectL(Marks):-
        write("\nC ::"),
        readint(C),
        write("\nC++ ::"),
        readint(CC),
        write("\nVB ::"),
        readint(VB),
        write("\nJAVA ::"),
        readint(Java),
        write("\nPROLOG ::"),
        readint(Prolog),
        Marks=[C,CC,VB,Java,Prolog].
    searchByName(Name1):-
        studentDB(Name1,Address,Phone,Marks),
        write("\nName::",Name1),
        write("\nAddress::",Address),
        write("\nPhone::",Phone),
        write("\nMarks[C,C++,VB,Java,Prolog]::",Marks).
    searchByPhone(Phone1):-
        studentDB(Name,Address,Phone1,Marks),
        write("\nName::",Name),
        write("\nAddress::",Address),
        write("\nPhone::",Phone1),
        write("\nMarks[C,C++,VB,Java,Prolog]::",Marks).