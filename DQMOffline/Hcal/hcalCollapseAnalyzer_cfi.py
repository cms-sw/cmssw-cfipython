import FWCore.ParameterSet.Config as cms

hcalCollapseAnalyzer = cms.EDProducer('HcalCollapseAnalyzer',
  topFolderName = cms.string('HcalCollapse'),
  verbosity = cms.untracked.int32(0),
  recHitHBHE = cms.untracked.InputTag('hbhereco'),
  preRecHitHBHE = cms.untracked.InputTag('hbheprereco'),
  doHE = cms.untracked.bool(True),
  doHB = cms.untracked.bool(False)
)
