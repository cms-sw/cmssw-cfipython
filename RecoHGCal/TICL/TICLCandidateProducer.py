import FWCore.ParameterSet.Config as cms

def TICLCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('TICLCandidateProducer',
    pluginInferenceAlgoTracksterInferenceByPFN = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/PFN/patternrecognition/id_v0.onnx'),
      onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/PFN/patternrecognition/energy_v0.onnx'),
      inputNames = cms.vstring(
        'input',
        'input_tr_features'
      ),
      output_en = cms.vstring('enreg_output'),
      output_id = cms.vstring('pid_output'),
      eid_min_cluster_energy = cms.double(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      doPID = cms.int32(1),
      doRegression = cms.int32(1),
      type = cms.string('TracksterInferenceByPFN')
    
    ),
    interpretationDescPSet = cms.PSet(
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
    regressionAndPid = cms.bool(True),
    inferenceAlgo = cms.string('TracksterInferenceByPFN'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
