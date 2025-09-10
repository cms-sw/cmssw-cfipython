import FWCore.ParameterSet.Config as cms

def HGCalCellUVTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalCellUVTester',
    waferSize = cms.double(166.4408),
    waferType = cms.int32(1),
    cellPlacementIndex = cms.int32(6),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
