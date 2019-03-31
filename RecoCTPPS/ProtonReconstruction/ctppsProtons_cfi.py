import FWCore.ParameterSet.Config as cms

ctppsProtons = cms.EDProducer('CTPPSProtonProducer',
  tagLocalTrackLite = cms.InputTag('ctppsLocalTrackLiteProducer'),
  lhcInfoLabel = cms.string(''),
  verbosity = cms.untracked.uint32(0),
  doSingleRPReconstruction = cms.bool(True),
  doMultiRPReconstruction = cms.bool(True),
  singleRPReconstructionLabel = cms.string('singleRP'),
  multiRPReconstructionLabel = cms.string('multiRP'),
  fitVtxY = cms.bool(True),
  useImprovedInitialEstimate = cms.bool(True)
)
