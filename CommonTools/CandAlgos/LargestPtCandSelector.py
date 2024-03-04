import FWCore.ParameterSet.Config as cms

def LargestPtCandSelector(**kwargs):
  mod = cms.EDFilter('LargestPtCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
