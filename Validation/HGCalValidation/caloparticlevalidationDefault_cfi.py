import FWCore.ParameterSet.Config as cms

caloparticlevalidationDefault = cms.EDAnalyzer('CaloParticleValidation',
  folder = cms.string('HGCAL/'),
  particles_to_monitor = cms.vint32(
    11,
    -11,
    13,
    22,
    111,
    211,
    -211,
    321,
    -321
  ),
  simVertices = cms.InputTag('g4SimHits'),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  simPFClusters = cms.InputTag('simPFProducer', 'perfect'),
  simPFCandidates = cms.InputTag('simPFProducer'),
  recHitsEE = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  recHitsFH = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  recHitsBH = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits')
)
