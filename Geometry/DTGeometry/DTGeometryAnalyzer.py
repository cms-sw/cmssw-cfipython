import FWCore.ParameterSet.Config as cms

def DTGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
