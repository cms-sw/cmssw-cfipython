import FWCore.ParameterSet.Config as cms

def HLTMuonRateAnalyzerWithWeight(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTMuonRateAnalyzerWithWeight',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
