import FWCore.ParameterSet.Config as cms

caloTowerMapTester = cms.EDAnalyzer('CaloTowerMapTester',
  mightGet = cms.optional.untracked.vstring
)
