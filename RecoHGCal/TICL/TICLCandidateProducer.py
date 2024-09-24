import FWCore.ParameterSet.Config as cms

def TICLCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('TICLCandidateProducer',
    interpretationDescPSet = cms.PSet(
      cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 1. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 5'),
      delta_tk_ts_layer1 = cms.double(0.02),
      delta_tk_ts_interface = cms.double(0.03),
      timing_quality_threshold = cms.double(0.5),
      algo_verbosity = cms.int32(0),
      type = cms.string('General')
    
    ),
    egamma_tracksters_collections = cms.VInputTag('ticlTracksterLinks'),
    egamma_tracksterlinks_collections = cms.VInputTag('ticlTracksterLinks'),
    general_tracksters_collections = cms.VInputTag('ticlTracksterLinks'),
    general_tracksterlinks_collections = cms.VInputTag('ticlTracksterLinks'),
    original_masks = cms.VInputTag('hgcalMergeLayerClusters:InitialLayerClustersMask'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_clustersTime = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    tracks = cms.InputTag('generalTracks'),
    timingSoA = cms.InputTag('mtdSoA'),
    muons = cms.InputTag('muons1stStep'),
    detector = cms.string('HGCAL'),
    propagator = cms.string('PropagatorWithMaterial'),
    useMTDTiming = cms.bool(True),
    useTimingAverage = cms.bool(True),
    timingQualityThreshold = cms.double(0.5),
    cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 1. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 5'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
