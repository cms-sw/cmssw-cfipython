import FWCore.ParameterSet.Config as cms

caloTowerTopologyTester = cms.EDAnalyzer('CaloTowerTopologyTester',
  mightGet = cms.optional.untracked.vstring
)
