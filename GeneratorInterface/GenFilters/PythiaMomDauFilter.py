import FWCore.ParameterSet.Config as cms

def PythiaMomDauFilter(**kwargs):
  mod = cms.EDFilter('PythiaMomDauFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
