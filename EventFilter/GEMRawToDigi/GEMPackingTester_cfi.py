import FWCore.ParameterSet.Config as cms

GEMPackingTester = cms.EDAnalyzer('GEMPackingTester',
  fed = cms.InputTag('rawDataCollector'),
  gemDigi = cms.InputTag('muonGEMDigis'),
  gemSimDigi = cms.InputTag('simMuonGEMDigis'),
  readMultiBX = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
