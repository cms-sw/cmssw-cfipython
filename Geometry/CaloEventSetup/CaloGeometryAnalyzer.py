import FWCore.ParameterSet.Config as cms

def CaloGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CaloGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
