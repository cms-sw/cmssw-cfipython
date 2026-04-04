import FWCore.ParameterSet.Config as cms

def ConcurrentIOVAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ConcurrentIOVAnalyzer',
    checkExpectedValues = cms.untracked.bool(True),
    fromSource = cms.untracked.ESInputTag('', ''),
    expectedESAcquireTestResults = cms.untracked.vint32(),
    expectedUniquePtrTestValue = cms.untracked.int32(0),
    expectedOptionalTestValue = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
