## AutoFSA

This repository contains Tool for verification and visualization of FAS's.

### Setup

1. Clone the repository:
      ```git clone https://github.com/peplxx/AutoFSA.git```
   

2. Install graphviz library:
      ```pip install graphviz```

3. Install [graphviz](https://www.graphviz.org/download/)
   

4. Write and run your code
   
   For clarification see examples.
   

### Features
- Provides functionality to create a Finite State Automaton (FSA).
- Support of 'and' and 'or' operations under two different fsa's.
- Allows definition of a different language set for the FSA.
- Includes methods to add start nodes, end nodes, and connecting edges between nodes with specific language components.
- Capable of rendering the FSA graph using graphviz library in various output formats (e.g., jpg).
- Checks for completeness of the FSA graph structure.
- Offers a clean and structured design for handling complex FSA workflows.
- Config for customization for different statuses of nodes.


### Gallary
* Green means entry node, red means end nodes
  
FSA Specification             |  Visualization
:-------------------------:|:-------------------------:
![image](https://github.com/peplxx/AutoFSA/assets/91543105/2bcefdd2-501b-485b-b4a4-0358429a3a42)  |  ![fsa1](https://github.com/peplxx/AutoFSA/assets/91543105/c618b100-e095-48be-bbe1-24134246d21e)
![image](https://github.com/peplxx/AutoFSA/assets/91543105/9bab6893-aec3-462c-b5c2-b17a6835075d) |  ![fsa2](https://github.com/peplxx/AutoFSA/assets/91543105/f97b375c-4318-44fc-b32c-dced907fc610)
![image](https://github.com/peplxx/AutoFSA/assets/91543105/46d56e9f-7782-48cf-ba34-d08f18cd8c8b) | ![fsa1 or fsa2](https://github.com/peplxx/AutoFSA/assets/91543105/fa403e3c-81b2-4b4b-b3d2-4f7016d71dd7)
![image](https://github.com/peplxx/AutoFSA/assets/91543105/df4d75a7-d6e1-444b-985f-a456e6a1916d) | ![fsa1 and fsa2](https://github.com/peplxx/AutoFSA/assets/91543105/47173ee4-c84a-4af3-910a-a0c863efec12)
![image](https://github.com/peplxx/AutoFSA/assets/91543105/85d98d43-f9fd-49a7-ac30-688e2be2fa11) | ![WordsFSA](https://github.com/peplxx/AutoFSA/assets/91543105/cc5ecce7-8f99-415e-9fc7-e7dd6b1ed7d1)



