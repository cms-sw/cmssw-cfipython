import FWCore.ParameterSet.Config as cms

def TrackerRecoGeometryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TrackerRecoGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
