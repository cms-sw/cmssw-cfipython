import FWCore.ParameterSet.Config as cms

l1tStage2RegionalMuonCandComp = cms.EDAnalyzer('L1TStage2RegionalMuonCandComp',
  monitorDir = cms.untracked.string(''),
  regionalMuonCollection1Title = cms.untracked.string('Regional muon collection 1'),
  regionalMuonCollection2Title = cms.untracked.string('Regional muon collection 2'),
  summaryTitle = cms.untracked.string('Summary'),
  ignoreBadTrackAddress = cms.untracked.bool(False),
  ignoreBin = cms.untracked.vint32(),
  verbose = cms.untracked.bool(False)
)
