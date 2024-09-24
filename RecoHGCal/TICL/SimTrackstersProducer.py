import FWCore.ParameterSet.Config as cms

def SimTrackstersProducer(*args, **kwargs):
  mod = cms.EDProducer('SimTrackstersProducer',
    detector = cms.string('HGCAL'),
    computeLocalTime = cms.bool(True),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    time_layerclusters = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    filtered_mask = cms.InputTag('filteredLayerClustersSimTracksters', 'ticlSimTracksters'),
    simclusters = cms.InputTag('mix', 'MergedCaloTruth'),
    caloparticles = cms.InputTag('mix', 'MergedCaloTruth'),
    MtdSimTracksters = cms.InputTag('mix', 'MergedMtdTruthST'),
    layerClusterSimClusterAssociator = cms.InputTag('layerClusterSimClusterAssociationProducer'),
    layerClusterCaloParticleAssociator = cms.InputTag('layerClusterCaloParticleAssociationProducer'),
    recoTracks = cms.InputTag('generalTracks'),
    cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 1. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 5'),
    tpToTrack = cms.InputTag('trackingParticleRecoTrackAsssociation'),
    trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
    simVertices = cms.InputTag('g4SimHits'),
    simTrackToTPMap = cms.InputTag('simHitTPAssocProducer', 'simTrackToTP'),
    fractionCut = cms.double(0),
    qualityCutTrack = cms.double(0.75),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod