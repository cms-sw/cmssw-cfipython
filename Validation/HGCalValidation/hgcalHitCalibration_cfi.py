import FWCore.ParameterSet.Config as cms

hgcalHitCalibration = cms.EDAnalyzer('HGCalHitCalibration',
  debug = cms.int32(0),
  rawRecHits = cms.bool(True),
  detector = cms.string('all'),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  recHitsEE = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  recHitsFH = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  recHitsBH = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
  hgcalMultiClusters = cms.InputTag('particleFlowClusterHGCalFromMultiCl'),
  electrons = cms.InputTag('ecalDrivenGsfElectronsFromMultiCl'),
  photons = cms.InputTag('photonsFromMultiCl')
)
