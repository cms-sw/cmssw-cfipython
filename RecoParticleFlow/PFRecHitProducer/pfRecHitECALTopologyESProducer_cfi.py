import FWCore.ParameterSet.Config as cms

pfRecHitECALTopologyESProducer = cms.ESProducer('PFRecHitECALTopologyESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
