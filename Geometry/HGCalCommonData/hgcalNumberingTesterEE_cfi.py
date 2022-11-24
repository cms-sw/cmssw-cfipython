import FWCore.ParameterSet.Config as cms

hgcalNumberingTesterEE = cms.EDAnalyzer('HGCalNumberingTester',
  NameSense = cms.string('HGCalEESensitive'),
  NameDevice = cms.string('HGCal EE'),
  LocalPositionX = cms.vdouble(),
  LocalPositionY = cms.vdouble(),
  Increment = cms.int32(19),
  DetType = cms.int32(2),
  Reco = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
