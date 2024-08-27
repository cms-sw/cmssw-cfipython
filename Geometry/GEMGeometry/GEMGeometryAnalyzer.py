import FWCore.ParameterSet.Config as cms

def GEMGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GEMGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
