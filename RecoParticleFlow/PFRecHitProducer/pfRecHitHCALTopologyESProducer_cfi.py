import FWCore.ParameterSet.Config as cms

pfRecHitHCALTopologyESProducer = cms.ESProducer('PFRecHitHCALTopologyESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
