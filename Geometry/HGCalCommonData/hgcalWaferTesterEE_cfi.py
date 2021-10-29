import FWCore.ParameterSet.Config as cms

hgcalWaferTesterEE = cms.EDAnalyzer('HGCalWaferTester',
  NameSense = cms.string('HGCalEESensitive'),
  NameDevice = cms.string('HGCal EE'),
  Reco = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
