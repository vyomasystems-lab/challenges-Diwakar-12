# Bubble sort module Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.
![Screenshot (34)](https://user-images.githubusercontent.com/77403373/180944951-42995623-3753-4604-b8f5-93061c57c8bd.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (bubble sort module here) which takes in 16-bit 5 inputs *in1* , *in2* , *in3* , *in4* and *in5* and gives 16-bit 5 outputs *out1* , *out2* , *out3* , *out4* and *out5* sorted in ascending order.

input constraints is from 0 to 2^16-1 which is 65535. ``` [0 to 65535] ```

The values are assigned to the input ports by getting the value from the user as follows: 
```
    a=int(input("enter 1st no :"))
    b=int(input("enter 2nd no :"))
    c=int(input("enter 3rd no :"))
    d=int(input("enter 4th no :"))
    e=int(input("enter 5th no :"))
    
    dut.in1.value = a
    dut.in2.value = b
    dut.in3.value = c
    dut.in4.value = d
    dut.in5.value = e
```

The assert statement is used for comparing the bubble sort model's output to the expected value.
```
 assert (dut.out1.value==list1[0]),"ERROR IN SORTING ELEMENTS expected {e5} in position 1 but got {k} ".format(e5=list1[0],k=hex(dut.out1.value))
 assert (dut.out2.value==list1[1]),"ERROR IN SORTING ELEMENTS expected {e5} in position 2 but got {k}".format(e5=list1[1],k=hex(dut.out2.value))
 assert (dut.out3.value==list1[2]),"ERROR IN SORTING ELEMENTS expected {e5} in position 3 but got {k} ".format(e5=list1[2],k=hex(dut.out3.value))
 assert (dut.out4.value==list1[3]),"ERROR IN SORTING ELEMENTS expected {e5} in position 4 but got {k} ".format(e5=list1[3],k=hex(dut.out4.value))
 assert (dut.out5.value==list1[4]),"ERROR IN SORTING ELEMENTS expected {e5} in position 5 but got {k}".format(e5=list1[4],k=hex(dut.out5.value))
```

## Correct Design 
Correct design running the test makes the test pass.
Here i have created a list of all the inputs in array ```list1=[a,b,c,d,e]``` and sorted for checking (validating) the DUT outputs 

![bubbbbb](https://user-images.githubusercontent.com/77403373/180991920-6c974933-1e9b-41f1-b637-3ff3272232ce.png)

The updated design is checked in as bubble.v

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 for (j = 1 ; j < i; j = j + 1) begin
          if (array[j] < array[j + 1])    =========> bug
          begin
            temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
  end end
```
In bubble sort module the swapping of inputs in array occurs when 1st number is greater than 2nd number.so the logic should be ``` (array[j] > array[j + 1]) ``` ,But the bug code is checking vice versa ``` (array[j] < array[j + 1]) ``` and sorting in descending order.

The following error is seen:
```
AssertionError: ERROR IN SORTING ELEMENTS expected 5 in position 1 but got 0x9 
```
## Test Scenario **(Important)**
- Here iam prompting the users for input values in test file python using int(input('Enter ith number'))

- Test Inputs: in1=9, in2=7, in3=6 ,in4=5, in5=4 i.e [9,8,7,6,5] .

- Expected Output: out1=5, out2=6, out3= 7, out4= 8, out5=9 i.e [5,6,7,8,9].

- Observed Output in the DUT : dut.out1.value=9 ,
                              dut.out2.value=8 ,
                              dut.out3.value= 7,
                              dut.out4.value=6,
                              dut.out5.value=5 
                              i.e [9,8,7,6,5].

Here the inpurts are 9,7,8,6,5 and the expected outputs are 5,6,7,8,9 but the DUT output is 9,8,7,6,5 .
Here we can see the input values are sorted in *descending aorder* but expected output is *ascending order* .
*Output mismatches for the above inputs proving that there is a design bug*


## Verification Strategy
-first assign all the inputs to the DUT

-then check correct for output

-validate with expected output

-do it for all combinations of inputs and check for expected outputs

-rectify the bugs

## Is the verification complete ?

yes ,checked for all combinations of input with constraints 0 to 65535 and validated the output values

