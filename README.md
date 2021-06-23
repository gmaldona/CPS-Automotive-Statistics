# CPS Automotive Statistics
Python script to get and log statistics for CPS-Automotive Research 

Tracks supported:
  - Straight Track: 
  ```python  
  trackPieces = ["StartPiece", "StraightPiece", "StraightPiece", "StraightPiece", "StraightPiece", "StartPiece", "CurvedPiece", "CurvedPiece", "StartPiece", "StraightPiece", "StraightPiece", "StraightPiece", "StraightPiece", "StartPiece", "CurvedPiece", "CurvedPiece"]
  start(track="straight") 
  ```
  - Oval Track:
  ```python
  trackPieces = ["StartPiece", "CurvedPiece", "CurvedPiece", "StraightPiece", "CurvedPiece", "CurvedPiece"]
  start(track="oval")
  ```
  - Figure-8
