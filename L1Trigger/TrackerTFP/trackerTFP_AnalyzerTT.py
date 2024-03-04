import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerTT(**kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerTT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
