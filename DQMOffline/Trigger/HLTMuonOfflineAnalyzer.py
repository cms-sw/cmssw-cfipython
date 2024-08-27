import FWCore.ParameterSet.Config as cms

def HLTMuonOfflineAnalyzer(**kwargs):
  mod = cms.EDProducer('HLTMuonOfflineAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
