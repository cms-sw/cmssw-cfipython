import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerTM(*args, **kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerTM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
