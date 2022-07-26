The verification environment is setup using Vyoma's UpTickPro provided for the hackathon

```screenshot of gitpod environment ```
![](https://user-images.githubusercontent.com/77403373/180925890-8932e808-45cd-43ae-b2ae-767de5f0f3ad.png)

## Verification Environment
The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (multiplexer module here) which takes in 5-bit input *sel* and 2-bit inputs from *inp1 to inp29* and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.inp1.value,dut.inp3.value,dut.inp5.value,dut.inp7.value,dut.inp9.value,dut.inp11.value,dut.inp13.value,dut.inp15.value,dut.inp17.value,dut.inp19.value,dut.inp21.value,dut.inp23.value,dut.inp25.value,dut.inp27.value,dut.inp29.value=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
dut.inp0.value,dut.inp2.value,dut.inp4.value,dut.inp6.value,dut.inp8.value,dut.inp10.value,dut.inp12.value,dut.inp14.value,dut.inp16.value,dut.inp18.value,dut.inp20.value,dut.inp22.value,dut.inp24.value,dut.inp26.value,dut.inp28.value,dut.inp30.value=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
```
Here inputs are assigned as for odd ports as 1 and for even ports as 0

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
![mux1](https://user-images.githubusercontent.com/77403373/180927562-420c3273-67a4-4398-adbb-dadc9a99a10b.png)
```
 AssertionError: failed for input select line 13,expected is 1
```
In the above error we found that ,for input select line 13 ,the DUT ouput was 0 but expected output for odd port is 1 as per my inputs.

## Test Scenario **(Important)**
1) BUG 1 *for select line 13*
- Test Inputs: sel=13
- Expected Output: out=1
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

2) BUG 2 *for select line 12*
- Test Inputs: sel=12
- Expected Output: out=0
- Observed Output in the DUT dut.out=0

Output matches for the above input but in code for port 12 output was not declared as input12.By default case output becomes 0'

## Design Bug
Based on the above test input and analysing the design, we see the following

-for bug in selectline 13
```
5'b01101: out = inp12;
```
For the mux design, the logic should be ``out=inp13`` instead of ``out=inp12`` as in the design code.

-for bug in selectline 12
```
5'b01101: out = inp12;
```
For the mux design, the logic should be ``sel=5'b01100`` instead of ``sel=5'b01101`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![mux2](https://user-images.githubusercontent.com/77403373/180928920-a689c77f-7540-4917-84c7-82ab203a39dc.png)

The updated design is checked in as mux_fix.v

## Verification Strategy
 -first assign all the inputs to the DUT
 
 -then check for random select line for output
 
 -validate with expected output
 
 -do it for all combinations of select lines and check for expected outputs
 
 -rectify the bugs
 
## Is the verification complete ?
 *Yes the verification is completed as it runned for selectline0 to  selectline 30 for correct output* 
