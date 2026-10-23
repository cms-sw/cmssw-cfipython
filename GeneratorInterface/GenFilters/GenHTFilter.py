import FWCore.ParameterSet.Config as cms

def GenHTFilter(*args, **kwargs):
  mod = cms.EDFilter('GenHTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
