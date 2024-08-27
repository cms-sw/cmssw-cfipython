import FWCore.ParameterSet.Config as cms

def CaloCellGeometryTester(**kwargs):
  mod = cms.EDAnalyzer('CaloCellGeometryTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
