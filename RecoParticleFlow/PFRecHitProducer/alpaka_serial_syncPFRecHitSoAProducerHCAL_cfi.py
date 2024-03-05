import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitSoAProducerHCAL = cms.EDProducer('alpaka_serial_sync::PFRecHitSoAProducerHCAL',
  producers = cms.VPSet(
    cms.PSet(
      src = cms.InputTag('')
    )
  ),
  topology = cms.ESInputTag('', ''),
  synchronise = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
