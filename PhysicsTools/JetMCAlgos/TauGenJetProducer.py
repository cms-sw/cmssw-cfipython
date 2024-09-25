import FWCore.ParameterSet.Config as cms

def TauGenJetProducer(*args, **kwargs):
  mod = cms.EDProducer('TauGenJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
