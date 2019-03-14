import FWCore.ParameterSet.Config as cms

l1tStage2uGMTMuon = cms.EDAnalyzer('L1TStage2uGMTMuon',
  monitorDir = cms.untracked.string(''),
  titlePrefix = cms.untracked.string(''),
  verbose = cms.untracked.bool(False)
)
