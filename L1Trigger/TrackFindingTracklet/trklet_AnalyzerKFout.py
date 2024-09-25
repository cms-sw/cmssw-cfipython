import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerKFout(*args, **kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerKFout',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
