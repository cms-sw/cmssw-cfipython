import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerKF(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerKF',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
