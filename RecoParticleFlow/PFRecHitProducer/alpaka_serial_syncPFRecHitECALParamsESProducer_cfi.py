import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitECALParamsESProducer = cms.ESProducer('alpaka_serial_sync::PFRecHitECALParamsESProducer',
  cleaningThreshold = cms.double(2),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
