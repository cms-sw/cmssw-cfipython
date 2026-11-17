import FWCore.ParameterSet.Config as cms

def HGCalCornerCheck(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalCornerCheck',
    Detector = cms.string('HGCalHEScintillatorSensitive'),
    LayerFirst = cms.int32(8),
    LayerLast = cms.int32(21),
    NMax = cms.uint32(2),
    Debug = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
