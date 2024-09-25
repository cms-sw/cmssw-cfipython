import FWCore.ParameterSet.Config as cms

def HcalGeometryDetIdTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalGeometryDetIdTester',
    DetectorMin = cms.int32(1),
    DetectorMax = cms.int32(4),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
