import FWCore.ParameterSet.Config as cms

def L2TauTagFilter(*args, **kwargs):
  mod = cms.EDFilter('L2TauTagFilter',
    saveTags = cms.bool(True),
    nExpected = cms.int32(2),
    L1TauSrc = cms.InputTag(''),
    L2Outcomes = cms.InputTag(''),
    DiscrWP = cms.double(0.1227),
    l1TauPtThreshold = cms.double(250),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
