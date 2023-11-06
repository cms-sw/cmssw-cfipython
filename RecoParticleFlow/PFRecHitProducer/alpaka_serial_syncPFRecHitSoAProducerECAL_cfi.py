import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitSoAProducerECAL = cms.EDProducer('alpaka_serial_sync::PFRecHitSoAProducerECAL',
  producers = cms.required.VPSet,
  topology = cms.required.ESInputTag,
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
