import FWCore.ParameterSet.Config as cms

def PythiaDauVFilter(**kwargs):
  mod = cms.EDFilter('PythiaDauVFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
