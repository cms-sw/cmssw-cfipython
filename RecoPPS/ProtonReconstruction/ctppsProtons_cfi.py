import FWCore.ParameterSet.Config as cms

ctppsProtons = cms.EDProducer('CTPPSProtonProducer',
  tagLocalTrackLite = cms.InputTag('ctppsLocalTrackLiteProducer'),
  pixelDiscardBXShiftedTracks = cms.bool(False),
  lhcInfoLabel = cms.string(''),
  opticsLabel = cms.string(''),
  ppsAssociationCutsLabel = cms.string(''),
  verbosity = cms.untracked.uint32(0),
  doSingleRPReconstruction = cms.bool(True),
  doMultiRPReconstruction = cms.bool(True),
  singleRPReconstructionLabel = cms.string('singleRP'),
  multiRPReconstructionLabel = cms.string('multiRP'),
  localAngleXMin = cms.double(-0.03),
  localAngleXMax = cms.double(0.03),
  localAngleYMin = cms.double(-0.04),
  localAngleYMax = cms.double(0.04),
  max_n_timing_tracks = cms.uint32(5),
  default_time = cms.double(0),
  fitVtxY = cms.bool(True),
  useImprovedInitialEstimate = cms.bool(True),
  multiRPAlgorithm = cms.string('chi2'),
  mightGet = cms.optional.untracked.vstring
)
