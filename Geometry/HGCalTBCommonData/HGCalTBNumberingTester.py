import FWCore.ParameterSet.Config as cms

def HGCalTBNumberingTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalTBNumberingTester',
    nameSense = cms.string('HGCalEESensitive'),
    nameDevice = cms.string('HGCal EE'),
    localPositionX = cms.vdouble(),
    localPositionY = cms.vdouble(),
    increment = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
