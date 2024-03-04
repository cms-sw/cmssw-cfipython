import FWCore.ParameterSet.Config as cms

def Hydjet2GeneratorFilter(**kwargs):
  mod = cms.EDFilter('Hydjet2GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
