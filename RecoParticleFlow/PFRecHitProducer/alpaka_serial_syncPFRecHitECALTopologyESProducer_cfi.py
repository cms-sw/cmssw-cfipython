import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitECALTopologyESProducer = cms.ESProducer('alpaka_serial_sync::PFRecHitECALTopologyESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
