import FWCore.ParameterSet.Config as cms

def HGCalPartialCellTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalPartialCellTester',
    waferSize = cms.double(166.4408),
    waferType = cms.int32(0),
    cellPlacementIndex = cms.int32(3),
    partialType = cms.int32(25),
    numbberOfTrials = cms.int32(1000),
    v17OrLess = cms.bool(False),
    modeUV = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod