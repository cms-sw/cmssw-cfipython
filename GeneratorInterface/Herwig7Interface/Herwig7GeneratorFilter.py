import FWCore.ParameterSet.Config as cms

def Herwig7GeneratorFilter(**kwargs):
  mod = cms.EDFilter('Herwig7GeneratorFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
