import FWCore.ParameterSet.Config as cms

def PythiaFilter(*args, **kwargs):
  mod = cms.EDFilter('PythiaFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
