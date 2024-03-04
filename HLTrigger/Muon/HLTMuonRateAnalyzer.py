import FWCore.ParameterSet.Config as cms

def HLTMuonRateAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HLTMuonRateAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
