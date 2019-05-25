import FWCore.ParameterSet.Config as cms

caloRecHitsBeamHaloCleaned = cms.EDProducer('CaloRecHitsBeamHaloCleaned',
  EBRecHitsLabel = cms.InputTag('EcalRecHit', 'EcalRecHitsEB'),
  EERecHitsLabel = cms.InputTag('EcalRecHit', 'EcalRecHitsEE'),
  HBHERecHitsLabel = cms.InputTag('hbhereco'),
  GlobalHaloDataLabel = cms.InputTag('GlobalHaloData'),
  IsHLT = cms.bool(False)
)
