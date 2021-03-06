import FWCore.ParameterSet.Config as cms

ctppsProtons = cms.EDProducer('CTPPSProtonProducer',
  tagLocalTrackLite = cms.InputTag('ctppsLocalTrackLiteProducer'),
  pixelDiscardBXShiftedTracks = cms.bool(False),
  lhcInfoLabel = cms.string(''),
  opticsLabel = cms.string(''),
  verbosity = cms.untracked.uint32(0),
  doSingleRPReconstruction = cms.bool(True),
  doMultiRPReconstruction = cms.bool(True),
  singleRPReconstructionLabel = cms.string('singleRP'),
  multiRPReconstructionLabel = cms.string('multiRP'),
  localAngleXMin = cms.double(-0.03),
  localAngleXMax = cms.double(0.03),
  localAngleYMin = cms.double(-0.04),
  localAngleYMax = cms.double(0.04),
  association_cuts_45 = cms.PSet(
    x_cut_apply = cms.bool(False),
    x_cut_mean = cms.double(0),
    x_cut_value = cms.double(0.0008),
    y_cut_apply = cms.bool(False),
    y_cut_mean = cms.double(0),
    y_cut_value = cms.double(0.0006),
    xi_cut_apply = cms.bool(True),
    xi_cut_mean = cms.double(0),
    xi_cut_value = cms.double(0.013),
    th_y_cut_apply = cms.bool(True),
    th_y_cut_mean = cms.double(0),
    th_y_cut_value = cms.double(2e-05),
    ti_tr_min = cms.double(-1),
    ti_tr_max = cms.double(1)
  ),
  association_cuts_56 = cms.PSet(
    x_cut_apply = cms.bool(False),
    x_cut_mean = cms.double(0),
    x_cut_value = cms.double(0.0008),
    y_cut_apply = cms.bool(False),
    y_cut_mean = cms.double(0),
    y_cut_value = cms.double(0.0006),
    xi_cut_apply = cms.bool(True),
    xi_cut_mean = cms.double(0),
    xi_cut_value = cms.double(0.013),
    th_y_cut_apply = cms.bool(True),
    th_y_cut_mean = cms.double(0),
    th_y_cut_value = cms.double(2e-05),
    ti_tr_min = cms.double(-1),
    ti_tr_max = cms.double(1)
  ),
  max_n_timing_tracks = cms.uint32(5),
  default_time = cms.double(0),
  fitVtxY = cms.bool(True),
  useImprovedInitialEstimate = cms.bool(True),
  multiRPAlgorithm = cms.string('chi2'),
  mightGet = cms.optional.untracked.vstring
)
