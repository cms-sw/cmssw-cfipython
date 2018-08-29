import FWCore.ParameterSet.Config as cms

electronIDValueMapProducer = cms.EDProducer('ElectronIDValueMapProducer',
  src = cms.InputTag('gedGsfElectrons'),
  srcMiniAOD = cms.InputTag('slimmedElectrons', '', '@skipCurrentProcess'),
  ebReducedRecHitCollection = cms.InputTag('reducedEcalRecHitsEB'),
  eeReducedRecHitCollection = cms.InputTag('reducedEcalRecHitsEE'),
  esReducedRecHitCollection = cms.InputTag('reducedEcalRecHitsES'),
  ebReducedRecHitCollectionMiniAOD = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
  eeReducedRecHitCollectionMiniAOD = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
  esReducedRecHitCollectionMiniAOD = cms.InputTag('reducedEgamma', 'reducedESRecHits')
)
