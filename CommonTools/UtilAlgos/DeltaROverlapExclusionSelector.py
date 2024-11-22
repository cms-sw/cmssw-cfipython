import FWCore.ParameterSet.Config as cms

def DeltaROverlapExclusionSelector(*args, **kwargs):
  mod = cms.EDFilter('DeltaROverlapExclusionSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
