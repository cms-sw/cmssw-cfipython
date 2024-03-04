import FWCore.ParameterSet.Config as cms

def HcalGeometryDetIdTester(**kwargs):
  mod = cms.EDAnalyzer('HcalGeometryDetIdTester',
    DetectorMin = cms.int32(1),
    DetectorMax = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
