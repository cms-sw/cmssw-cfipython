import FWCore.ParameterSet.Config as cms

def HGCalGeometryCornerTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryCornerTester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
