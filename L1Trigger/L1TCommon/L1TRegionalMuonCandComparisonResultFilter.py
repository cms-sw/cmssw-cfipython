import FWCore.ParameterSet.Config as cms

def L1TRegionalMuonCandComparisonResultFilter(**kwargs):
  mod = cms.EDFilter('L1TRegionalMuonCandComparisonResultFilter',
    objComparisonColl = cms.InputTag('objComparisonColl'),
    maxBxRangeDiff = cms.int32(-1),
    maxExcess = cms.int32(-1),
    maxSize = cms.int32(-1),
    invert = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
