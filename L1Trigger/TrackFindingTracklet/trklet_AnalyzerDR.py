import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerDR(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerDR',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
