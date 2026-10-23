import FWCore.ParameterSet.Config as cms

def MCProcessRangeFilter(*args, **kwargs):
  mod = cms.EDFilter('MCProcessRangeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
