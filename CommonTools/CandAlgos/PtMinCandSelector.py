import FWCore.ParameterSet.Config as cms

def PtMinCandSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinCandSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
