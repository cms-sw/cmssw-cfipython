import FWCore.ParameterSet.Config as cms

def IsTBH4Type(*args, **kwargs):
  mod = cms.EDFilter('IsTBH4Type',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
