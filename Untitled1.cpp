
#include <iostream>
#define fd(x) for(digits[x]=0;digits[x]<10;digits[x]++)
int get_first_digit(int digits[])
{
    int first_digit = 0;
    for(int x=8;x>=0;x--)
    {
        if(digits[x]!=0)
        {
            first_digit = x;
            return first_digit;
        }
    }
}
int main()
{
    int digits[9] = {0,0,0,0,0,0,0,0};
    int bound=0;
    int run_count=0;
    int reversible_count = 0;
    fd(8)
    {
        fd(7)
        {
            fd(6)
            {
                //std::cout << "WTF\n";
                fd(5)
                {
                    fd(4)
                    {
                        fd(3)
                        {
                            fd(2)
                            {
                                fd(1)
                                {
                                    int first_digit = get_first_digit(digits);
                                    if(first_digit==0)
                                    {
                                        bound=1;
                                    }
                                    else
                                    {
                                        //bound = 2;
                                        bound=digits[first_digit];
                                    }

                                    for(digits[0]=bound;digits[0]<10;digits[0]++)
                                    {

                                        run_count++;

                                        // check for oddness
                                        int carry_num = 0;
                                        int all_odd = true;
                                        for(int x=0; x<=first_digit; x++)
                                        {
                                            int sum_num = digits[x] + digits[first_digit-x] + carry_num;

                                            if(sum_num %2 == 0){all_odd = false; break;}
                                            else
                                            {
                                                if(sum_num>10){carry_num = 1;} else{carry_num = 0;}
                                            }
                                        }
                                        //TODO: check for palindrome
                                        bool is_palindrome = true;
                                        if(all_odd)
                                        {
                                            for(int x=0; x<=first_digit; x++ )
                                            {
                                                if(x==first_digit-x)
                                                {
                                                    continue;
                                                }
                                                else
                                                {
                                                    if(digits[x] != digits[first_digit - x])
                                                    {
                                                        is_palindrome = false;
                                                    }
                                                }
                                            }
                                            if(is_palindrome){reversible_count++;}
                                            else             {reversible_count+=2;}

                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }




    std::cout << "Run Count: " << run_count << "\n";
    std::cout << "Rev Count: " << reversible_count<< "\n";
    return 0;
}
