import FWCore.ParameterSet.Config as cms

from .L1TGlobalSummary import L1TGlobalSummary

L1TGlobalSummary = L1TGlobalSummary(
  AlgInputTag = ('gtStage2Digis'),
  ExtInputTag = ('gtStage2Digis'),
  MinBx = -2,
  MaxBx = 2,
  DumpTrigResults = False,
  DumpRecord = False,
  DumpTrigSummary = True,
  ReadPrescalesFromFile = False,
  psFileName = 'prescale_L1TGlobal.csv',
  psColumn = 0
)
