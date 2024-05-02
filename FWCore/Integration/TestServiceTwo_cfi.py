import FWCore.ParameterSet.Config as cms

TestServiceTwo = cms.Service('TestServiceTwo',
  verbose = cms.untracked.bool(False),
  printTimestamps = cms.untracked.bool(False)
)
