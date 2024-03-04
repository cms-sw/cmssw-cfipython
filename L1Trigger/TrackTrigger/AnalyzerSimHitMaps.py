import FWCore.ParameterSet.Config as cms

def AnalyzerSimHitMaps(**kwargs):
  mod = cms.EDAnalyzer('AnalyzerSimHitMaps',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
