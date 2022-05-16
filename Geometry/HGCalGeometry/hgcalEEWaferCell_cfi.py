import FWCore.ParameterSet.Config as cms

hgcalEEWaferCell = cms.EDAnalyzer('HGCalWaferCell',
  NameSense = cms.string('HGCalEESensitive'),
  NameDevice = cms.string('HGCal EE'),
  Verbosity = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
