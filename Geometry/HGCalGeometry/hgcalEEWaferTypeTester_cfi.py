import FWCore.ParameterSet.Config as cms

hgcalEEWaferTypeTester = cms.EDAnalyzer('HGCalWaferTypeTester',
  NameSense = cms.string('HGCalEESensitive'),
  NameDevice = cms.string('HGCal EE'),
  mightGet = cms.optional.untracked.vstring
)
