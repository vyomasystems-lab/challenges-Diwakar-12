## Sequence Detector 1011 Design Verification


The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://user-images.githubusercontent.com/77403373/180925890-8932e808-45cd-43ae-b2ae-767de5f0f3ad.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect module here) which takes in 1-bit input *inp_bit* and  gives 1-bit output *seq_seen*

The values are assigned to the input port using 
```
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=0
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
    dut.inp_bit.value=1
    await FallingEdge(dut.clk)
```

The assert statement is used for comparing the seq-detect's ouput to the expected value.
![seq error](https://user-images.githubusercontent.com/77403373/180990433-a1629db2-0282-4ca3-b3e8-ed4146ead3b9.png)


The following error is seen:
```
    assert dut.seq_seen.value==1,"bug for input stream identified {input} expected output {out}".format(input=11011,out=1)
    AssertionError: bug for input stream identified 11011 expected output 1
```

## Test Scenario 
- Test Inputs: inp_bit=11011
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen=0

For overlapping on non-sequence the output for 11011 should give output 1 but DUT output was 0.
Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

-BUG 1

```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;        ======> bug
        else
          next_state = SEQ_10;
      end
```
For the sequence detect design, the logic is if ithe current state is seq1 and  if input 1 is given means then the next state should be the same state  ``next_state=SEQ_1`` instead of ``IDLE`` as in the design code for non sequence overlapping case.

This identification of bug in sequence detector is corrected using *state diagram* realization for requires application of non-sequence overlapping
 
 Bug Fixed code
```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end
```

 
## Design Fix
Updating the design and re-running the test makes the test pass.

![seq](https://user-images.githubusercontent.com/77403373/180933959-72363e91-c101-4363-a492-c0bdbeddf50e.png)

The updated design is checked in as seqdetect_fix.v

## Verification Strategy

- check for inputs randomly and validate with expected value of output

- check for given input condition for non-sequence overlapping reference input 11011 and compare the outputs 

- rectify the bug using state diagram diagnosis
 
 - execute for rectified code and see the outputs

## Is the verification complete ?

