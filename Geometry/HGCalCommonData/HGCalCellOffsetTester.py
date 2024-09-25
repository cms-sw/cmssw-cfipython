import FWCore.ParameterSet.Config as cms

def HGCalCellOffsetTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalCellOffsetTester',
    waferSize = cms.double(167.4408),
    waferType = cms.int32(0),
    cellPlacementIndex = cms.int32(11),
    cellType = cms.int32(0),
    mouseBiteCut = cms.double(5),
    guardRingOffset = cms.double(0.9),
    sizeOffset = cms.double(0.435),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
