import FWCore.ParameterSet.Config as cms

l1tStage2uGMT = cms.EDAnalyzer('L1TStage2uGMT',
  monitorDir = cms.untracked.string(''),
  emulator = cms.untracked.bool(False),
  verbose = cms.untracked.bool(False)
)
