bool isI(char c)
{
    return c == 'I';
}

bool isV(char c)
{
    return c == 'V';
}

bool isX(char c)
{
    return c == 'X';
}

bool isL(char c)
{
    return c == 'L';
}

bool isC(char c)
{
    return c == 'C';
}

bool isD(char c)
{
    return c == 'D';
}

bool isM(char c)
{
    return c == 'M';
}


int romanToInt(char * s)
{
    int nb = 0;
    int i = 0;
    while (*s != '\0') {
        if (isI(*s)) {
            if (isV(s[1])) {
                s++;
                nb += 4;
            } else if (isX(s[1])) {
                s++;
                nb += 9;
            } else
                nb += 1;
        } else if (isV(*s))
            nb += 5;
        else if (isX(*s)) {
            if (isL(s[1])) {
                s++;
                nb += 40;
            } else if (isC(s[1])) {
                s++;
                nb += 90;
            } else
                nb += 10;
        } else if (isL(*s))
            nb += 50;
        else if (isC(*s)) {
            if (isD(s[1])) {
                s++;
                nb += 400;
            } else if (isM(s[1])) {
                s++;
                nb += 900;
            } else 
               nb += 100;
        } else if (isD(*s))
            nb += 500;
        else if (isM(*s))
            nb += 1000;
        s++;
    }
    return (nb);
}