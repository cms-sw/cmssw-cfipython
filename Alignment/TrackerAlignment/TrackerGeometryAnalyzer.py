import FWCore.ParameterSet.Config as cms

def TrackerGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackerGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
