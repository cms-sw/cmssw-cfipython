import FWCore.ParameterSet.Config as cms

def TauValJetViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValJetViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
