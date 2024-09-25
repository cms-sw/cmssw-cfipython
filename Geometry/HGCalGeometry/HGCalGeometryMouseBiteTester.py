import FWCore.ParameterSet.Config as cms

def HGCalGeometryMouseBiteTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryMouseBiteTester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
