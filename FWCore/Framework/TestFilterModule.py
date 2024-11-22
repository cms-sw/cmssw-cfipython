import FWCore.ParameterSet.Config as cms

def TestFilterModule(*args, **kwargs):
  mod = cms.EDFilter('TestFilterModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
