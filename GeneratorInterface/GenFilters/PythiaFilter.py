import FWCore.ParameterSet.Config as cms

def PythiaFilter(**kwargs):
  mod = cms.EDFilter('PythiaFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
