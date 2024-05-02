import FWCore.ParameterSet.Config as cms

TestServiceOne = cms.Service('TestServiceOne',
  verbose = cms.untracked.bool(False),
  printTimestamps = cms.untracked.bool(False)
)
