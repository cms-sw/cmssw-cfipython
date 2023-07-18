import FWCore.ParameterSet.Config as cms

hgcalTBNumberingTesterEE = cms.EDAnalyzer('HGCalTBNumberingTester',
  nameSense = cms.string('HGCalEESensitive'),
  nameDevice = cms.string('HGCal EE'),
  localPositionX = cms.vdouble(),
  localPositionY = cms.vdouble(),
  increment = cms.int32(2),
  mightGet = cms.optional.untracked.vstring
)
