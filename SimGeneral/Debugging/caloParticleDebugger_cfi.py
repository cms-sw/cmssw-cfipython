import FWCore.ParameterSet.Config as cms

caloParticleDebugger = cms.EDAnalyzer('CaloParticleDebugger',
  simTracks = cms.InputTag('g4SimHits'),
  genParticles = cms.InputTag('genParticles'),
  simVertices = cms.InputTag('g4SimHits'),
  trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
  collectionTags = cms.VInputTag(
    'g4SimHits:HGCHitsEE',
    'g4SimHits:HGCHitsHEfront',
    'g4SimHits:HcalHits'
  ),
  mightGet = cms.optional.untracked.vstring
)
