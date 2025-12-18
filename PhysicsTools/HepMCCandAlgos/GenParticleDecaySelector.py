import FWCore.ParameterSet.Config as cms

def GenParticleDecaySelector(*args, **kwargs):
  mod = cms.EDProducer('GenParticleDecaySelector',
    src = cms.required.InputTag,
    particle = cms.required.int32,
    status = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
