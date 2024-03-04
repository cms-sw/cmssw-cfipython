import FWCore.ParameterSet.Config as cms

def DeltaROverlapExclusionSelector(**kwargs):
  mod = cms.EDFilter('DeltaROverlapExclusionSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
