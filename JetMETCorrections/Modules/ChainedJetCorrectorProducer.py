import FWCore.ParameterSet.Config as cms

def ChainedJetCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('ChainedJetCorrectorProducer',
    correctors = cms.required.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
