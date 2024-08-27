import FWCore.ParameterSet.Config as cms

def HGCalGeometryTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalGeometryTester',
    Detector = cms.string('HGCalEESensitive'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
