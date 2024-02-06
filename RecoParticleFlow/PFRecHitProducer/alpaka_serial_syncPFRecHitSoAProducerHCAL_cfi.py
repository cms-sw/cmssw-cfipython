import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitSoAProducerHCAL = cms.EDProducer('alpaka_serial_sync::PFRecHitSoAProducerHCAL',
  producers = cms.required.VPSet,
  topology = cms.required.ESInputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
