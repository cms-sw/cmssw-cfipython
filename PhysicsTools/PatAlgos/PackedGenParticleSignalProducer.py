import FWCore.ParameterSet.Config as cms

def PackedGenParticleSignalProducer(*args, **kwargs):
  mod = cms.EDProducer('PackedGenParticleSignalProducer',
    genParticles = cms.InputTag('genParticles'),
    packedGenParticles = cms.InputTag('packedGenParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
