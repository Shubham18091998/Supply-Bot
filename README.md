# Supply-Bot
e-Yantra Robotics Competition (eYRC 2019-20)
Task 4 – Supply Bot
The aim of this task is to integrate your image processing knowledge acquired in the previous
tasks with the provided hardware to build a robot to traverse the arena and solve/complete the
task.
Problem Statement:
Given the Capital shown in Fig. 1. below and the Configuration Table in Table 1, the built
Supply Bot using Image Processing should traverse the arena to reach the City where the
Medical Aid is ready for dispatch. Hit/Strike the Medical Aid just once so that it moves
across the Dead Zone and reaches the White circular region traversing the respective Villages
for maximum outreach via the City Nodes’s Sector.
Fig. 1.
Note: Please follow the arena setup instruction as provided in the RuleBook
The Capital is the Node directly above the ‘t’ of the e-Yantra logo (highlighted by the blue
arrow).
Node Type Node Number
Medical Aid 6
Table 1. Configuration Table
The Configuration Table indicates the placement of the Red coin (Medical Aid); which is
depicted in Fig. 2. for your reference:
Fig. 2.
For your reference, the various Correct deposits are depicted in Figures 3-5 below. The goal
is to strike the coin in such a manner that it goes beyond the Dead Zone and lands in the
Orange sector in front of the Dead Zone or White circle at the center of the Arena.
Fig. 3. Valid Deposit (Eg.1)
Note: The Supply Bot should not stop at every City on the way to the City with the
requirement of the Medical Aid.
In Summary,
1. On running the Python script from the console, the script should output the node
number of the City requiring the Aid, on the console.
2. The laptop running the Python Script should communicate with Supply Bot over
XBee.
3. The Supply Bot will then, start at the Capital traverse the Highway (white line) to
reach the City in need of Medical Aid.
4. Stop at the City, beep the buzzer twice, and dispatch with one time contact the
Medical Aid towards the Villages with need.
5. Once the Medical Aid reaches the Village(s) beyond the Dead Zone, the Supply Bot
beeps the buzzer once as an acknowledgment for aid dispatch.
6. The Supply Bot should now return to the Capital and beep the buzzer to indicate the
end of the run as given in the Rulebook.
Fig. 4. Valid Deposit (Eg.2)
Fig. 5. Valid Deposit (Eg.3)
The Medical Aid is rendered useless and lost if it reaches and stops in the Dead Zone or
Lake. There is no score and one penalty will be imposed when in Dead Zone. Also no score
for landing in the lake part of the sector in front of which the Medical Aid is placed; however
there will be no penalty for landing in the Lake.
----------------------------------------------------------------------------------------------------------------
