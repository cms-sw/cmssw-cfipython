import FWCore.ParameterSet.Config as cms

def PerfectGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PerfectGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
