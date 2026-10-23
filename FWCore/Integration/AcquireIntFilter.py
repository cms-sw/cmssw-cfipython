import FWCore.ParameterSet.Config as cms

def AcquireIntFilter(*args, **kwargs):
  mod = cms.EDFilter('AcquireIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
