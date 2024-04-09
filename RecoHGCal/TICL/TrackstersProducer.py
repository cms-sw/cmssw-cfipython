import FWCore.ParameterSet.Config as cms

def TrackstersProducer(**kwargs):
  mod = cms.EDProducer('TrackstersProducer',
    detector = cms.string('HGCAL'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    filtered_mask = cms.InputTag('filteredLayerClusters', 'iterationLabelGoesHere'),
    original_mask = cms.InputTag('hgcalMergeLayerClusters', 'InitialLayerClustersMask'),
    time_layerclusters = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    layer_clusters_tiles = cms.InputTag('ticlLayerTileProducer'),
    layer_clusters_hfnose_tiles = cms.InputTag('ticlLayerTileHFNose'),
    seeding_regions = cms.InputTag('ticlSeedingRegionProducer'),
    patternRecognitionBy = cms.string('CA'),
    itername = cms.string('unknown'),
    tfDnnLabel = cms.string('tracksterSelectionTf'),
    pluginPatternRecognitionByCA = cms.PSet(
      algo_verbosity = cms.int32(0),
      oneTracksterPerTrackSeed = cms.bool(False),
      promoteEmptyRegionToTrackster = cms.bool(False),
      out_in_dfs = cms.bool(True),
      max_out_in_hops = cms.int32(10),
      min_cos_theta = cms.double(0.915),
      min_cos_pointing = cms.double(-1),
      root_doublet_max_distance_from_seed_squared = cms.double(9999),
      etaLimitIncreaseWindow = cms.double(2.1),
      skip_layers = cms.int32(0),
      max_missing_layers_in_trackster = cms.int32(9999),
      shower_start_max_layer = cms.int32(9999),
      min_layers_per_trackster = cms.int32(10),
      filter_on_categories = cms.vint32(0),
      pid_threshold = cms.double(0),
      energy_em_over_total_threshold = cms.double(-1),
      max_longitudinal_sigmaPCA = cms.double(9999),
      max_delta_time = cms.double(3),
      eid_input_name = cms.string('input'),
      eid_output_name_energy = cms.string('output/regressed_energy'),
      eid_output_name_id = cms.string('output/id_probabilities'),
      eid_min_cluster_energy = cms.double(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      siblings_maxRSquared = cms.vdouble(
        0.0006,
        0.0006,
        0.0006
      ),
      type = cms.string('CA')
    
    ),
    pluginPatternRecognitionByCLUE3D = cms.PSet(
      algo_verbosity = cms.int32(0),
      criticalDensity = cms.double(4),
      criticalSelfDensity = cms.double(0.15),
      densitySiblingLayers = cms.int32(3),
      densityEtaPhiDistanceSqr = cms.double(0.0008),
      densityXYDistanceSqr = cms.double(3.24),
      kernelDensityFactor = cms.double(0.2),
      densityOnSameLayer = cms.bool(False),
      nearestHigherOnSameLayer = cms.bool(False),
      useAbsoluteProjectiveScale = cms.bool(True),
      useClusterDimensionXY = cms.bool(False),
      rescaleDensityByZ = cms.bool(False),
      criticalEtaPhiDistance = cms.double(0.025),
      criticalXYDistance = cms.double(1.8),
      criticalZDistanceLyr = cms.int32(5),
      outlierMultiplier = cms.double(2),
      minNumLayerCluster = cms.int32(2),
      eid_input_name = cms.string('input'),
      eid_output_name_energy = cms.string('output/regressed_energy'),
      eid_output_name_id = cms.string('output/id_probabilities'),
      eid_min_cluster_energy = cms.double(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      type = cms.string('CLUE3D')
    
    ),
    pluginPatternRecognitionByFastJet = cms.PSet(
      algo_verbosity = cms.int32(0),
      antikt_radius = cms.double(0.09),
      minNumLayerCluster = cms.int32(5),
      eid_input_name = cms.string('input'),
      eid_output_name_energy = cms.string('output/regressed_energy'),
      eid_output_name_id = cms.string('output/id_probabilities'),
      eid_min_cluster_energy = cms.double(1),
      eid_n_layers = cms.int32(50),
      eid_n_clusters = cms.int32(10),
      type = cms.string('FastJet')
    
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod