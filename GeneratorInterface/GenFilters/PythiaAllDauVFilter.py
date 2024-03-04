import FWCore.ParameterSet.Config as cms

def PythiaAllDauVFilter(**kwargs):
  mod = cms.EDFilter('PythiaAllDauVFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
