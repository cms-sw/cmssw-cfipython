import FWCore.ParameterSet.Config as cms

alpaka_serial_syncPFRecHitHCALParamsESProducer = cms.ESProducer('alpaka_serial_sync::PFRecHitHCALParamsESProducer',
  energyThresholdsHB = cms.vdouble(
    0.1,
    0.2,
    0.3,
    0.3
  ),
  energyThresholdsHE = cms.vdouble(
    0.1,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2,
    0.2
  ),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
