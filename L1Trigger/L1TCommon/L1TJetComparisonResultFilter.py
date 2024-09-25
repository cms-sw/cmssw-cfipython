import FWCore.ParameterSet.Config as cms

def L1TJetComparisonResultFilter(*args, **kwargs):
  mod = cms.EDFilter('L1TJetComparisonResultFilter',
    objComparisonColl = cms.InputTag('objComparisonColl'),
    maxBxRangeDiff = cms.int32(-1),
    maxExcess = cms.int32(-1),
    maxSize = cms.int32(-1),
    invert = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
