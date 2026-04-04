import FWCore.ParameterSet.Config as cms

def MCProcessFilter(*args, **kwargs):
  mod = cms.EDFilter('MCProcessFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
