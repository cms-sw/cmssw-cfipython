import FWCore.ParameterSet.Config as cms

legacyPFRecHitProducer = cms.EDProducer('LegacyPFRecHitProducer',
  src = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
