import FWCore.ParameterSet.Config as cms

def L1DEFilter(*args, **kwargs):
  mod = cms.EDFilter('L1DEFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
