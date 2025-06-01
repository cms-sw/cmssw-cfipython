import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerKF(*args, **kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerKF',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
