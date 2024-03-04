import FWCore.ParameterSet.Config as cms

def PythiaFilterTTBar(**kwargs):
  mod = cms.EDFilter('PythiaFilterTTBar',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
