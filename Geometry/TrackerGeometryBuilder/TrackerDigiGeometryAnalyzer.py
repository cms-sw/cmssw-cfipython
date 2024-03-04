import FWCore.ParameterSet.Config as cms

def TrackerDigiGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackerDigiGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
