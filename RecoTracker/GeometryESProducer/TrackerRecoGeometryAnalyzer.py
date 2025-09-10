import FWCore.ParameterSet.Config as cms

def TrackerRecoGeometryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackerRecoGeometryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
