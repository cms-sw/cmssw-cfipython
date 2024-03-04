import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerKFout(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerKFout',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
