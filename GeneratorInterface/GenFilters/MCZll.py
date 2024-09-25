import FWCore.ParameterSet.Config as cms

def MCZll(*args, **kwargs):
  mod = cms.EDFilter('MCZll',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
