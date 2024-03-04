import FWCore.ParameterSet.Config as cms

def TrackstersMergeProducerV3(**kwargs):
  mod = cms.EDProducer('TrackstersMergeProducerV3',
    tracksterstrkem = cms.InputTag('ticlTrackstersTrkEM'),
    trackstersem = cms.InputTag('ticlTrackstersEM'),
    tracksterstrk = cms.InputTag('ticlTrackstersTrk'),
    trackstershad = cms.InputTag('ticlTrackstersHAD'),
    seedingTrk = cms.InputTag('ticlSeedingTrk'),
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    layer_clustersTime = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
    tracks = cms.InputTag('generalTracks'),
    optimiseAcrossTracksters = cms.bool(True),
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
    eid_min_cluster_energy = cms.double(1),
    eid_n_layers = cms.int32(50),
    eid_n_clusters = cms.int32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
