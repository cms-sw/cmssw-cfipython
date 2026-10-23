import FWCore.ParameterSet.Config as cms

def HLTMuonRateAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTMuonRateAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
