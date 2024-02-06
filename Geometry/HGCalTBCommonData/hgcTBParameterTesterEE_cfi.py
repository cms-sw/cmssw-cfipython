import FWCore.ParameterSet.Config as cms

hgcTBParameterTesterEE = cms.EDAnalyzer('HGCalTBParameterTester',
  name = cms.string('HGCalEESensitive'),
  mode = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
