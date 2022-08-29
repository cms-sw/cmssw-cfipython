import FWCore.ParameterSet.Config as cms

packedGenParticlesSignal = cms.EDProducer('PackedGenParticleSignalProducer',
  genParticles = cms.InputTag('genParticles'),
  packedGenParticles = cms.InputTag('packedGenParticles'),
  mightGet = cms.optional.untracked.vstring
)
