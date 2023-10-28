import FWCore.ParameterSet.Config as cms

pfRecHitECALParamsESProducer = cms.ESProducer('PFRecHitECALParamsESProducer@alpaka',
  cleaningThreshold = cms.double(2),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
