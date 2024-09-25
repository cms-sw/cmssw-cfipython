import FWCore.ParameterSet.Config as cms

def HLTTauDQMOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTTauDQMOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
