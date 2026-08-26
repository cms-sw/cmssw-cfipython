import FWCore.ParameterSet.Config as cms

def TrackstersProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackstersProducer',
    detector = cms.string('HGCAL'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    filtered_mask = cms.InputTag('filteredLayerClusters', 'iterationLabelGoesHere'),
    original_mask = cms.InputTag('hgcalMergeLayerClusters', 'InitialLayerClustersMask'),
    time_layerclusters = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    layer_clusters_tiles = cms.InputTag('ticlLayerTileProducer'),
    layer_clusters_barrel_tiles = cms.InputTag('ticlLayerTileProducer', 'ticlLayerTilesBarrel'),
    layer_clusters_hfnose_tiles = cms.InputTag('ticlLayerTileHFNose'),
    seeding_regions = cms.InputTag('ticlSeedingRegionProducer'),
    patternRecognitionBy = cms.string('CLUE3D'),
    itername = cms.string('unknown'),
    inferenceAlgo = cms.string(''),
    pluginPatternRecognitionByCA = cms.PSet(
      algo_verbosity = cms.int32(0),
      oneTracksterPerTrackSeed = cms.bool(False),
      promoteEmptyRegionToTrackster = cms.bool(False),
      out_in_dfs = cms.bool(True),
      max_out_in_hops = cms.int32(10),
      min_cos_theta = cms.float(0.915),
      min_cos_pointing = cms.float(-1),
      root_doublet_max_distance_from_seed_squared = cms.float(9999),
      etaLimitIncreaseWindow = cms.float(2.1),
      skip_layers = cms.int32(0),
      max_missing_layers_in_trackster = cms.int32(9999),
      shower_start_max_layer = cms.int32(9999),
      min_layers_per_trackster = cms.int32(10),
      filter_on_categories = cms.vint32(0),
      pid_threshold = cms.float(0),
      energy_em_over_total_threshold = cms.float(-1),
      max_longitudinal_sigmaPCA = cms.float(9999),
      max_delta_time = cms.float(3),
      computeLocalTime = cms.bool(True),
      siblings_maxRSquared = cms.vfloat(
        0.0006,
        0.0006,
        0.0006
      ),
      type = cms.string('CA')
    
    ),
    pluginPatternRecognitionByCLUE3D = cms.PSet(
      algo_verbosity = cms.int32(0),
      criticalDensity = cms.vfloat(
        4,
        4,
        4
      ),
      criticalSelfDensity = cms.vfloat(
        0.15,
        0.15,
        0.15
      ),
      densitySiblingLayers = cms.vint32(
        3,
        3,
        3
      ),
      densityEtaPhiDistanceSqr = cms.vfloat(
        0.0008,
        0.0008,
        0.0008
      ),
      densityXYDistanceSqr = cms.vfloat(
        3.24,
        3.24,
        3.24
      ),
      kernelDensityFactor = cms.vfloat(
        0.2,
        0.2,
        0.2
      ),
      densityOnSameLayer = cms.bool(False),
      nearestHigherOnSameLayer = cms.bool(False),
      useAbsoluteProjectiveScale = cms.bool(True),
      useClusterDimensionXY = cms.bool(False),
      rescaleDensityByZ = cms.bool(False),
      criticalEtaPhiDistance = cms.vfloat(
        0.025,
        0.025,
        0.025
      ),
      criticalXYDistance = cms.vfloat(
        1.8,
        1.8,
        1.8
      ),
      criticalZDistanceLyr = cms.vint32(
        5,
        5,
        5
      ),
      outlierMultiplier = cms.vfloat(
        2,
        2,
        2
      ),
      minNumLayerCluster = cms.vint32(
        2,
        2,
        2
      ),
      doPidCut = cms.bool(False),
      cutHadProb = cms.float(0.5),
      computeLocalTime = cms.bool(True),
      usePCACleaning = cms.bool(True),
      type = cms.string('CLUE3D')
    
    ),
    pluginPatternRecognitionByFastJet = cms.PSet(
      algo_verbosity = cms.int32(0),
      antikt_radius = cms.float(0.09),
      minNumLayerCluster = cms.int32(5),
      computeLocalTime = cms.bool(True),
      type = cms.string('FastJet')
    
    ),
    pluginPatternRecognitionByRecovery = cms.PSet(
      algo_verbosity = cms.int32(0),
      type = cms.string('Recovery')
    
    ),
    pluginInferenceAlgoTracksterInferenceByDNN = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxPIDModelPath = cms.string(''),
      onnxEnergyModelPath = cms.string(''),
      inputNames = cms.vstring('input'),
      output_en = cms.vstring('enreg_output'),
      output_id = cms.vstring('pid_output'),
      eid_min_cluster_energy = cms.float(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      doPID = cms.int32(1),
      doRegression = cms.int32(1),
      miniBatchSize = cms.untracked.int32(64),
      type = cms.string('TracksterInferenceByDNN')
    
    ),
    pluginInferenceAlgoTracksterInferenceByCNN = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxModelPath = cms.string('RecoHGCal/TICL/data/ticlv5/onnx_models/CNN/patternrecognition/id_v0.onnx'),
      inputNames = cms.vstring('input'),
      outputNames = cms.vstring('pid_output'),
      eid_min_cluster_energy = cms.float(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      doPID = cms.int32(1),
      miniBatchSize = cms.untracked.int32(64),
      type = cms.string('TracksterInferenceByCNN')
    
    ),
    pluginInferenceAlgoTracksterInferenceByPFN = cms.PSet(
      algo_verbosity = cms.int32(0),
      onnxPIDModelPath = cms.string(''),
      onnxEnergyModelPath = cms.string(''),
      inputNames = cms.vstring(
        'input',
        'input_tr_features'
      ),
      output_en = cms.vstring('enreg_output'),
      output_id = cms.vstring('pid_output'),
      eid_min_cluster_energy = cms.float(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      doPID = cms.int32(1),
      doRegression = cms.int32(1),
      miniBatchSize = cms.untracked.int32(64),
      type = cms.string('TracksterInferenceByPFN')
    
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
