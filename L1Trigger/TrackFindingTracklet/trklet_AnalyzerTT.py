import FWCore.ParameterSet.Config as cms

def trklet_AnalyzerTT(**kwargs):
  mod = cms.EDAnalyzer('trklet::AnalyzerTT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
