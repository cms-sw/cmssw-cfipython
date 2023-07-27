import FWCore.ParameterSet.Config as cms

hgcalPartialIDTesterEE = cms.EDAnalyzer('HGCalPartialIDTester',
  nameDetector = cms.string('HGCalEESensitive'),
  fileName = cms.string('partialD98.txt'),
  debug = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
