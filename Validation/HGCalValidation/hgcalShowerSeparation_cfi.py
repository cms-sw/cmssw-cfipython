import FWCore.ParameterSet.Config as cms

hgcalShowerSeparation = cms.EDProducer('HGCalShowerSeparation',
  debug = cms.int32(1),
  filterOnEnergyAndCaloP = cms.bool(False),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  recHitsEE = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  recHitsFH = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  recHitsBH = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits')
)
