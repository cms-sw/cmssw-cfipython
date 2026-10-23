import FWCore.ParameterSet.Config as cms

def APVShotsFilter(*args, **kwargs):
  mod = cms.EDFilter('APVShotsFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
