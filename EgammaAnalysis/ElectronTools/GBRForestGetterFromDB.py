import FWCore.ParameterSet.Config as cms

def GBRForestGetterFromDB(**kwargs):
  mod = cms.EDAnalyzer('GBRForestGetterFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
