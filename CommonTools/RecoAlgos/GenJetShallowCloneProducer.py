import FWCore.ParameterSet.Config as cms

def GenJetShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('GenJetShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
