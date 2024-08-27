import FWCore.ParameterSet.Config as cms

def GenParticleDecaySelector(**kwargs):
  mod = cms.EDProducer('GenParticleDecaySelector',
    src = cms.required.InputTag,
    particle = cms.required.int32,
    status = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
