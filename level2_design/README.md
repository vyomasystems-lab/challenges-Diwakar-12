# MUX Design Verification

The verification environment is setup using Vyoma's UpTickPro provided for the hackathon

```screenshot of gitpod environment ```
![](https://user-images.githubusercontent.com/77403373/180925890-8932e808-45cd-43ae-b2ae-767de5f0f3ad.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (bitmanipulation coprocessor module here) which takes in 32-bit 4 inputs *mav_putvalue_instr, mav_putvalue_src1,mav_putvalue_src2, mav_putvalue_src3* and  outputs 33-bit *mav_putvalue*

The values are assigned to the input ports using 
```
 maximum_number= 2**32   #for maximum range of inputs for 32 bits is 2^32-1 , for loop runs for n-1 value only  
    for i in range(maximum_number):
        mav_putvalue_src1 = i
        mav_putvalue_src2 = i
        mav_putvalue_src3 = i
        mav_putvalue_instr = 0x101010B3
```
Here firstly i have initiated the inputs by giving same inputs to all the ports to check for error which has 2^32 combinations initially.
The assert statement is used for comparing the DUT's outut to the expected model value.

The following error is seen:
![bitmanip](https://user-images.githubusercontent.com/77403373/181562583-2711a97f-b114-4a57-9072-0360c0ff216f.png)

 ```AssertionError: For inputs =(1, 1, 1) Value mismatch DUT = 0x2 does not match MODEL = 0x0```

In the above error we found that ,for inputs 1,1,1 for 3 inputs and instruction of 0x101010B3 ,the DUT ouput was 0x2 but expected model output is 0x0.

## Test Scenario **(Important)**
The *first error* found  for input combination of 1,1,1 and instruction 0x101010B3 
1) BUG 1 *inputs 1,1,1 and instruction 0x101010B3*
- Test Inputs:        mav_putvalue_src1 = 1
                      mav_putvalue_src2 = 1
                      mav_putvalue_src3 = 1
                      mav_putvalue_instr = 0x101010B3 
- Expected Output: out=0x0
- Observed Output in the DUT dut.out=0x2

Output mismatches for the above inputs proving that there is a design bug


## Verification Strategy
 -first assign all the possible inputs to the DUT
 
 -then check for model output to the DUT output
 
 -validate with expected output
 
 
## Is the verification complete ?
 *No, the verification is not completed as it turned out that first error found for certain combination of input ,as it is sufficient finding one bug , the first bug is exxposed here* 

