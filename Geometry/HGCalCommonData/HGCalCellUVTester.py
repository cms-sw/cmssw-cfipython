import FWCore.ParameterSet.Config as cms

def HGCalCellUVTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalCellUVTester',
    waferSize = cms.double(166.4408),
    waferType = cms.int32(1),
    cellPlacementIndex = cms.int32(6),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
