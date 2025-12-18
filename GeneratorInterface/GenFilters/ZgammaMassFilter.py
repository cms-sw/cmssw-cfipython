import FWCore.ParameterSet.Config as cms

def ZgammaMassFilter(*args, **kwargs):
  mod = cms.EDFilter('ZgammaMassFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
