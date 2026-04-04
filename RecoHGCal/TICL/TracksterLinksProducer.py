import FWCore.ParameterSet.Config as cms

def TracksterLinksProducer(*args, **kwargs):
  mod = cms.EDProducer('TracksterLinksProducer',
    pluginInferenceAlgoTracksterInferenceByDNN = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxPIDModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/patternrecognition/id_v0.onnx'),
      onnxEnergyModelPath = cms.FileInPath('RecoHGCal/TICL/data/ticlv5/onnx_models/DNN/patternrecognition/energy_v0.onnx'),
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
      cylinder_radius_sqr_split = cms.double(9),
      proj_distance_split = cms.double(5),
      track_time_quality_threshold = cms.double(0.5),
      min_num_lcs = cms.uint32(7),
      min_trackster_energy = cms.double(10),
      pca_quality_th = cms.double(0.85),
      dot_prod_th = cms.double(0.97),
      deltaRxy = cms.double(4),
      lower_boundary = cms.vdouble(
        10,
        150
      ),
      upper_boundary = cms.vdouble(
        3,
        70
      ),
      upper_distance_projective_sqr = cms.vdouble(
        40,
        60
      ),
      lower_distance_projective_sqr = cms.vdouble(
        10,
        30
      ),
      min_distance_z = cms.vdouble(
        35,
        35
      ),
      upper_distance_projective_sqr_closest_points = cms.vdouble(
        10,
        30
      ),
      lower_distance_projective_sqr_closest_points = cms.vdouble(
        10,
        30
      ),
      max_z_distance_closest_points = cms.vdouble(
        35,
        35
      ),
      cylinder_radius_sqr = cms.vdouble(
        10,
        20
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
    inferenceAlgo = cms.string('TracksterInferenceByPFN'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
