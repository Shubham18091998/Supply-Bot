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
Along with this document, we have provided possible cases (.PNG files), and the total score
for each of the cases. Please follow the “Rule Book Modification” file for the formula and
additional important points.
Possible sample cases enlisted are scored in the table below for your reference of Scoring:
Fig.6. Case 1.
Case 1 Explained:
Node 3: Food Supply
Node 6: Medical Aid
Node 9: Food Supply
Assuming the path traversal (Node Sequence) to be: Node 3 -> Node 6 -> Node 9 -> Node 1
and assuming 300 seconds of run time for all cases (Case 1,.....Case 5)
Scoring is as follows:
NH = 1 (NH for Node 9 is the only Valid NH)
CD = 3 (Since all Relief Aids were dispatched (successfully or not), assuming stop and beeps
at all nodes here)
P = 1 since the Medical Aid (Red Coin) is overlapping a Dead Zone
B = 0 since a Penalty has occurred
CB = 0 since no RElief Aid is in the innermost White Village
Case Node
Sequence
TT RT NH CD P B CB Total
Case1.jpg 3,6,9,1 480 300 1 3 1 0 0 330
Table 2. Scoring Case1, Path Assumption 1
Similarly, for the same Case 1; another path of Node traversal can be made.
Assuming the Path Traversal (Node Sequence) to be: Node 6 -> Node 9 -> Node 3 -> Node 1
and assuming 300 seconds of run time for all cases
Scoring is as follows:
NH = 1 (NH for Node 9 is the only Valid NH)
CD = 3 (Since all Relief Aids were dispatched (successfully or not), assuming stop and beeps
at all nodes here)
P = 1 since the Medical Aid (Red Coin) is overlapping a Dead Zone
B = 0 since a Penalty has occurred
CB = 0 since no Relief Aid is in the innermost White Village
Case Node
Sequence
TT RT NH CD P B CB Total
Case1.jpg 6,9,3,1 480 300 1 3 1 0 0 330
Table 3. Scoring Case 1, Path Assumption 2
Similarly, referring to Table 4 and diagrams of the Cases 2 to 5, you can infer scores by
identifying the assumed Path Traversal (Node Sequence).
Fig.7. Case 2.
Fig.8. Case 3.
Fig.9. Case 4.
Fig.10. Case 5. (Cropped View)
Case Node
Sequence
TT RT NH CD P B CB Total
Case1.jpg 3,6,9,1 480 300 1 3 1 0 0 330
Case1.jpg 6,9,3,1 480 300 1 3 1 0 0 330
Case2.jpg 3,6,9,1 480 300 2 3 1 0 1 505
Case2.jpg 6,9,3,1 480 300 2 3 1 0 1 505
Case3.jpg 3,6,9,1 480 300 2 3 1 0 2 580
Case3.jpg 3,6,9,1 480 300 2 2 2 0 2 510
Case3.jpg 6,9,3,1 480 300 2 3 1 0 2 580
Case3.jpg 6,9,3,1 480 300 2 2 2 0 2 510
Case4.jpg 3,6,9,1 480 300 3 3 0 1 3 796
Case4.jpg 6,9,3,1 480 300 3 3 0 1 4 871
Case5.jpg 3,6,9,1 480 300 0 3 1 0 0 230
Case5.jpg 6,9,3,1 480 300 0 3 1 0 0 230
Table 4. Scoring
