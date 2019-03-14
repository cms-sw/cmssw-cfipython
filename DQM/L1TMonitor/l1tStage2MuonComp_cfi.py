import FWCore.ParameterSet.Config as cms

l1tStage2MuonComp = cms.EDAnalyzer('L1TStage2MuonComp',
  monitorDir = cms.untracked.string(''),
  muonCollection1Title = cms.untracked.string('Muon collection 1'),
  muonCollection2Title = cms.untracked.string('Muon collection 2'),
  summaryTitle = cms.untracked.string('Summary'),
  ignoreBin = cms.untracked.vint32(),
  verbose = cms.untracked.bool(False)
)
