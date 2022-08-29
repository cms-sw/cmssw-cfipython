import FWCore.ParameterSet.Config as cms

hgcalGeometryTesterEE = cms.EDAnalyzer('HGCalGeometryTester',
  Detector = cms.string('HGCalEESensitive'),
  mightGet = cms.optional.untracked.vstring
)
