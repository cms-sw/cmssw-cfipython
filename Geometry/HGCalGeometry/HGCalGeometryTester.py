import FWCore.ParameterSet.Config as cms

def HGCalGeometryTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryTester',
    Detector = cms.string('HGCalEESensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
