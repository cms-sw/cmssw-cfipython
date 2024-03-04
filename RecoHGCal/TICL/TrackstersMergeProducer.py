import FWCore.ParameterSet.Config as cms

def TrackstersMergeProducer(**kwargs):
  mod = cms.EDProducer('TrackstersMergeProducer',
    linkingPSet = cms.PSet(
      cutTk = cms.string('1.48 < abs(eta) < 3.0 && pt > 1. && quality("highPurity") && hitPattern().numberOfLostHits("MISSING_OUTER_HITS") < 5'),
      delta_tk_ts_layer1 = cms.double(0.02),
      delta_tk_ts_interface = cms.double(0.03),
      delta_ts_em_had = cms.double(0.03),
      delta_ts_had_had = cms.double(0.03),
      track_time_quality_threshold = cms.double(0.5),
      algo_verbosity = cms.int32(0),
      type = cms.string('LinkingAlgoByDirectionGeometric')
    
    ),
    trackstersclue3d = cms.InputTag('ticlTrackstersCLUE3DHigh'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_clustersTime = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    tracks = cms.InputTag('generalTracks'),
    tracksTime = cms.InputTag('tofPID', 't0'),
    tracksTimeQual = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    tracksTimeErr = cms.InputTag('tofPID', 'sigmat0'),
    muons = cms.InputTag('muons1stStep'),
    detector = cms.string('HGCAL'),
    propagator = cms.string('PropagatorWithMaterial'),
    optimiseAcrossTracksters = cms.bool(True),
    useMTDTiming = cms.bool(True),
    eta_bin_window = cms.int32(1),
    phi_bin_window = cms.int32(1),
    pt_sigma_high = cms.double(2),
    pt_sigma_low = cms.double(2),
    halo_max_distance2 = cms.double(4),
    track_min_pt = cms.double(1),
    track_min_eta = cms.double(1.48),
    track_max_eta = cms.double(3),
    track_max_missing_outerhits = cms.int32(5),
    cosangle_align = cms.double(0.9945),
    e_over_h_threshold = cms.double(1),
    pt_neutral_threshold = cms.double(2),
    resol_calo_offset_had = cms.double(1.5),
    resol_calo_scale_had = cms.double(0.15),
    resol_calo_offset_em = cms.double(1.5),
    resol_calo_scale_em = cms.double(0.15),
    tfDnnLabel = cms.string('tracksterSelectionTf'),
    eid_input_name = cms.string('input'),
    eid_output_name_energy = cms.string('output/regressed_energy'),
    eid_output_name_id = cms.string('output/id_probabilities'),
    eid_min_cluster_energy = cms.double(2.5),
    eid_n_layers = cms.int32(50),
    eid_n_clusters = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
