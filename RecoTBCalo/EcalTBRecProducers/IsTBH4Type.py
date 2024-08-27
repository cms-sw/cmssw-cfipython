import FWCore.ParameterSet.Config as cms

def IsTBH4Type(**kwargs):
  mod = cms.EDFilter('IsTBH4Type',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
