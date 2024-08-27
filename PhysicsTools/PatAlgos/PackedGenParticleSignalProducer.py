import FWCore.ParameterSet.Config as cms

def PackedGenParticleSignalProducer(**kwargs):
  mod = cms.EDProducer('PackedGenParticleSignalProducer',
    genParticles = cms.InputTag('genParticles'),
    packedGenParticles = cms.InputTag('packedGenParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
