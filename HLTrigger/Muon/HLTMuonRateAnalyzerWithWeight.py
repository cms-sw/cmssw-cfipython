import FWCore.ParameterSet.Config as cms

def HLTMuonRateAnalyzerWithWeight(**kwargs):
  mod = cms.EDAnalyzer('HLTMuonRateAnalyzerWithWeight',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
