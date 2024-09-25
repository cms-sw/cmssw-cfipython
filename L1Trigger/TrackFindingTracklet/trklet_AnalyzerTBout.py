import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerTBout(*args, **kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerTBout',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
