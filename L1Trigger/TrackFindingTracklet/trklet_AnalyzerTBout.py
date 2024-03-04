import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerTBout(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerTBout',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
