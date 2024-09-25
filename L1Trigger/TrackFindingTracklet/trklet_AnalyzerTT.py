import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerTT(*args, **kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerTT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
