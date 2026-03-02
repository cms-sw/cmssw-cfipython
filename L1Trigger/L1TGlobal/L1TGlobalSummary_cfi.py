import FWCore.ParameterSet.Config as cms

from .L1TGlobalSummary import L1TGlobalSummary

L1TGlobalSummary = L1TGlobalSummary(

  AlgInputTag = ('gtStage2Digis'),
  ExtInputTag = ('gtStage2Digis'),
  MaxBx = 2,
  MinBx = -2
)
