import FWCore.ParameterSet.Config as cms

def TiclDebugger(*args, **kwargs):
  mod = cms.EDAnalyzer('TiclDebugger',
    trackstersMerge = cms.InputTag('ticlTrackstersMerge'),
    tracks = cms.InputTag('generalTracks'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
