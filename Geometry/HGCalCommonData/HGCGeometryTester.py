import FWCore.ParameterSet.Config as cms

def HGCGeometryTester(**kwargs):
  mod = cms.EDAnalyzer('HGCGeometryTester',
    SquareType = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
