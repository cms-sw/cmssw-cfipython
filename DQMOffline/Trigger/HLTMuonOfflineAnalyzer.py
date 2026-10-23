import FWCore.ParameterSet.Config as cms

def HLTMuonOfflineAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HLTMuonOfflineAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
