import FWCore.ParameterSet.Config as cms

pfRecHitHCALParamsESProducer = cms.ESProducer('PFRecHitHCALParamsESProducer@alpaka',
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
