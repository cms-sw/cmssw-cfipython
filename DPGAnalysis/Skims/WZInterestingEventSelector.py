import FWCore.ParameterSet.Config as cms

def WZInterestingEventSelector(*args, **kwargs):
  mod = cms.EDFilter('WZInterestingEventSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
