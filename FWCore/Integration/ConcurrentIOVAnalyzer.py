import FWCore.ParameterSet.Config as cms

def ConcurrentIOVAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ConcurrentIOVAnalyzer',
    checkExpectedValues = cms.untracked.bool(True),
    fromSource = cms.untracked.ESInputTag('', ''),
    expectedESAcquireTestResults = cms.untracked.vint32(),
    expectedUniquePtrTestValue = cms.untracked.int32(0),
    expectedOptionalTestValue = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
