import FWCore.ParameterSet.Config as cms

def RandomFilter(*args, **kwargs):
  mod = cms.EDFilter('RandomFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
