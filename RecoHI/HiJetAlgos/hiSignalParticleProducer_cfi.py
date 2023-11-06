import FWCore.ParameterSet.Config as cms

hiSignalParticleProducer = cms.EDProducer('HiSignalParticleProducer',
  src = cms.InputTag('genParticles'),
  mightGet = cms.optional.untracked.vstring
)
