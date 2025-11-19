import FWCore.ParameterSet.Config as cms

def HGCalGeomLocaterTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalGeomLocaterTester',
    detector = cms.string('HGCalEESensitive'),
    stepSilicon = cms.uint32(10),
    stepScintillator = cms.uint32(10),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
