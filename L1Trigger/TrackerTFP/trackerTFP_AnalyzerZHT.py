import FWCore.ParameterSet.Config as cms

def trackerTFP_AnalyzerZHT(**kwargs):
  mod = cms.EDAnalyzer('trackerTFP::AnalyzerZHT',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
