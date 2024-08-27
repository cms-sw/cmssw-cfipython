import FWCore.ParameterSet.Config as cms

def PythiaDauFilter(**kwargs):
  mod = cms.EDFilter('PythiaDauFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
