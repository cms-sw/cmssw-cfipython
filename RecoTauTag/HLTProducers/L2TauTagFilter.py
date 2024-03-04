import FWCore.ParameterSet.Config as cms

def L2TauTagFilter(**kwargs):
  mod = cms.EDFilter('L2TauTagFilter',
    saveTags = cms.bool(True),
    nExpected = cms.int32(2),
    L1TauSrc = cms.InputTag(''),
    L2Outcomes = cms.InputTag(''),
    DiscrWP = cms.double(0.1227),
    l1TauPtThreshold = cms.double(250),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
