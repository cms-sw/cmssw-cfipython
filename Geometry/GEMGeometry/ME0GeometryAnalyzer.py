import FWCore.ParameterSet.Config as cms

def ME0GeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ME0GeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
