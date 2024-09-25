import FWCore.ParameterSet.Config as cms

def ComphepSingletopFilterPy8(*args, **kwargs):
  mod = cms.EDFilter('ComphepSingletopFilterPy8',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
