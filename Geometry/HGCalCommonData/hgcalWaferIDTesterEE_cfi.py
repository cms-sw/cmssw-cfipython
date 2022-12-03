import FWCore.ParameterSet.Config as cms

hgcalWaferIDTesterEE = cms.EDAnalyzer('HGCalWaferIDTester',
  nameSense = cms.string('HGCalEESensitive'),
  fileName = cms.string('cellIDEE.txt'),
  mightGet = cms.optional.untracked.vstring
)
