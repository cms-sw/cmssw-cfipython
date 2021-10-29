import FWCore.ParameterSet.Config as cms

hgcalEEWaferInFileTest = cms.EDAnalyzer('HGCalWaferInFileTest',
  NameSense = cms.string('HGCalEESensitive'),
  NameDevice = cms.string('HGCal EE'),
  Verbosity = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
