import FWCore.ParameterSet.Config as cms

def HGCalTBNumberingTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalTBNumberingTester',
    nameSense = cms.string('HGCalEESensitive'),
    nameDevice = cms.string('HGCal EE'),
    localPositionX = cms.vdouble(),
    localPositionY = cms.vdouble(),
    increment = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
