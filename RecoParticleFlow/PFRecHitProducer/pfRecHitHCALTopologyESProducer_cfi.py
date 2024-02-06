import FWCore.ParameterSet.Config as cms

pfRecHitHCALTopologyESProducer = cms.ESProducer('PFRecHitHCALTopologyESProducer@alpaka',
  usePFThresholdsFromDB = cms.bool(True),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
