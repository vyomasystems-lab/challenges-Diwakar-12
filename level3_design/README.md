# Bubble sort module Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (bubble sort module here) which takes in 15-bit inputs *in1* , *in2* , *in3* , *in4* and *in5* and gives 15-bit outputs *out1* , *out2* , *out3* , *out4* and *out5* sorted in ascending order.

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

The following error is seen:
```

```
