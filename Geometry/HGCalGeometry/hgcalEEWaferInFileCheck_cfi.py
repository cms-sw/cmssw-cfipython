import FWCore.ParameterSet.Config as cms

hgcalEEWaferInFileCheck = cms.EDAnalyzer('HGCalWaferInFileCheck',
  NameSense = cms.string('HGCalEESensitive'),
  NameDevice = cms.string('HGCal EE'),
  mightGet = cms.optional.untracked.vstring
)
