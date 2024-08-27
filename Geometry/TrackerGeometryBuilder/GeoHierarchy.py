import FWCore.ParameterSet.Config as cms

def GeoHierarchy(**kwargs):
  mod = cms.EDAnalyzer('GeoHierarchy',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
