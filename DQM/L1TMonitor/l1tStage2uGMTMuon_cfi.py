import FWCore.ParameterSet.Config as cms

l1tStage2uGMTMuon = cms.EDProducer('L1TStage2uGMTMuon',
  muonProducer = cms.required.InputTag,
  monitorDir = cms.untracked.string(''),
  titlePrefix = cms.untracked.string(''),
  verbose = cms.untracked.bool(False),
  makeMuonAtVtxPlots = cms.untracked.bool(False),
  displacedQuantities = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
