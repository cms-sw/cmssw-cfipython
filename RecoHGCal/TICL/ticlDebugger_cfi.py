import FWCore.ParameterSet.Config as cms

ticlDebugger = cms.EDAnalyzer('TiclDebugger',
  trackstersMerge = cms.InputTag('ticlTrackstersMerge'),
  tracks = cms.InputTag('generalTracks'),
  caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
  layerClusters = cms.InputTag('hgcalLayerClusters'),
  mightGet = cms.optional.untracked.vstring
)
