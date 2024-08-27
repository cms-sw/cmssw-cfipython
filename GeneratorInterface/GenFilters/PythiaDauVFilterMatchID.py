import FWCore.ParameterSet.Config as cms

def PythiaDauVFilterMatchID(**kwargs):
  mod = cms.EDFilter('PythiaDauVFilterMatchID',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
