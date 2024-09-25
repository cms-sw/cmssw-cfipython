import FWCore.ParameterSet.Config as cms

def TrackerDigiGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackerDigiGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
