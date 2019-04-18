import FWCore.ParameterSet.Config as cms

L1TGlobalSummary = cms.EDAnalyzer('L1TGlobalSummary',
  AlgInputTag = cms.InputTag(''),
  ExtInputTag = cms.InputTag(''),
  MinBx = cms.int32(0),
  MaxBx = cms.int32(0),
  DumpTrigResults = cms.bool(False),
  DumpRecord = cms.bool(False),
  DumpTrigSummary = cms.bool(True)
)
