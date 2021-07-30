import FWCore.ParameterSet.Config as cms

hgcParameterTesterEE = cms.EDAnalyzer('HGCalParameterTester',
  Name = cms.string('HGCalEESensitive'),
  Mode = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
