import FWCore.ParameterSet.Config as cms

def LargestPtCandSelector(*args, **kwargs):
  mod = cms.EDFilter('LargestPtCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
