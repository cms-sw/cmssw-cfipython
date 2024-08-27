import FWCore.ParameterSet.Config as cms

def TestGetterOfProducts(**kwargs):
  mod = cms.EDFilter('TestGetterOfProducts',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
