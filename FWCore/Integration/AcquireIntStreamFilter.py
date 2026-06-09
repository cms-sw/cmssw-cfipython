import FWCore.ParameterSet.Config as cms

def AcquireIntStreamFilter(*args, **kwargs):
  mod = cms.EDFilter('AcquireIntStreamFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
