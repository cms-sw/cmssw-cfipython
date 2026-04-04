import FWCore.ParameterSet.Config as cms

def GenVisTauProducer(*args, **kwargs):
  mod = cms.EDProducer('GenVisTauProducer',
    src = cms.required.InputTag,
    srcGenParticles = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
