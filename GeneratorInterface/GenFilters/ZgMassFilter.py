import FWCore.ParameterSet.Config as cms

def ZgMassFilter(*args, **kwargs):
  mod = cms.EDFilter('ZgMassFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
