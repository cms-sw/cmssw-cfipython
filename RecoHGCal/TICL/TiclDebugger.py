import FWCore.ParameterSet.Config as cms

def TiclDebugger(**kwargs):
  mod = cms.EDAnalyzer('TiclDebugger',
    trackstersMerge = cms.InputTag('ticlTrackstersMerge'),
    tracks = cms.InputTag('generalTracks'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
