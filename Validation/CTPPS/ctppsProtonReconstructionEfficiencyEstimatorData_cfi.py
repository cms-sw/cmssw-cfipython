import FWCore.ParameterSet.Config as cms

ctppsProtonReconstructionEfficiencyEstimatorData = cms.EDAnalyzer('CTPPSProtonReconstructionEfficiencyEstimatorData',
  tagTracks = cms.InputTag(''),
  tagRecoProtonsMultiRP = cms.InputTag(''),
  pixelDiscardBXShiftedTracks = cms.bool(False),
  localAngleXMin = cms.double(-0.03),
  localAngleXMax = cms.double(0.03),
  localAngleYMin = cms.double(-0.04),
  localAngleYMax = cms.double(0.04),
  opticsLabel = cms.string(''),
  n_prep_events = cms.uint32(1000),
  n_exp_prot_max = cms.uint32(5),
  n_sigmas = cms.vdouble(
    3,
    5,
    7
  ),
  rpId_45_N = cms.uint32(0),
  rpId_45_F = cms.uint32(0),
  rpId_56_N = cms.uint32(0),
  rpId_56_F = cms.uint32(0),
  outputFile = cms.string('output.root'),
  verbosity = cms.untracked.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
