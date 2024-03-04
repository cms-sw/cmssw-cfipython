import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerGP(**kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerGP',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
