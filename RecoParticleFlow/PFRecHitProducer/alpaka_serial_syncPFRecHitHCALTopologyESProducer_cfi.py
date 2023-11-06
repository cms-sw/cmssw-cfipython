import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitHCALTopologyESProducer = cms.ESProducer('alpaka_serial_sync::PFRecHitHCALTopologyESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
