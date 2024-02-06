import FWCore.ParameterSet.Config as cms

pfRecHitECALTopologyESProducer = cms.ESProducer('PFRecHitECALTopologyESProducer@alpaka',
  usePFThresholdsFromDB = cms.bool(False),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
