import FWCore.ParameterSet.Config as cms

def TracksterLinksProducer(*args, **kwargs):
  mod = cms.EDProducer('TracksterLinksProducer',
    pluginInferenceAlgoTracksterInferenceByDNN = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/patternrecognition/id_v0.onnx'),
      onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/patternrecognition/energy_v0.onnx'),
      inputNames = cms.vstring('input'),
      output_en = cms.vstring('enreg_output'),
      output_id = cms.vstring('pid_output'),
      eid_min_cluster_energy = cms.double(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      doPID = cms.int32(1),
      doRegression = cms.int32(1),
      type = cms.string('TracksterInferenceByDNN')
    
    ),
    pluginInferenceAlgoTracksterInferenceByCNNv4 = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv4/onnx_models/energy_id_v0.onnx'),
      inputNames = cms.vstring('input:0'),
      outputNames = cms.vstring(
        'output/regressed_energy:0',
        'output/id_probabilities:0'
      ),
      eid_min_cluster_energy = cms.double(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      doPID = cms.int32(1),
      doRegression = cms.int32(0),
      type = cms.string('TracksterInferenceByCNNv4')
    
    ),
    linkingPSet = cms.PSet(
      track_time_quality_threshold = cms.double(0.5),
      wind = cms.double(0.036),
      min_num_lcs = cms.uint32(7),
      min_trackster_energy = cms.double(10),
      pca_quality_th = cms.double(0.85),
      dot_prod_th = cms.double(0.97),
      max_distance_projective_sqr = cms.vdouble(
        60,
        60
      ),
      min_distance_z = cms.vdouble(
        30,
        30
      ),
      max_distance_projective_sqr_closest_points = cms.vdouble(
        60,
        60
      ),
      max_z_distance_closest_points = cms.vdouble(
        35,
        35
      ),
      cylinder_radius_sqr = cms.vdouble(
        9,
        9
      ),
      algo_verbosity = cms.int32(0),
      type = cms.string('Skeletons')
    
    ),
    tracksters_collections = cms.VInputTag('ticlTrackstersCLUE3DHigh'),
    original_masks = cms.VInputTag('hgcalMergeLayerClusters:InitialLayerClustersMask'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_clustersTime = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    regressionAndPid = cms.bool(False),
    detector = cms.string('HGCAL'),
    propagator = cms.string('PropagatorWithMaterial'),
    inferenceAlgo = cms.string('TracksterInferenceByDNN'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
