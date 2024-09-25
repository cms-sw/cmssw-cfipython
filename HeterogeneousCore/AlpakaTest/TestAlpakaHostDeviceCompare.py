import FWCore.ParameterSet.Config as cms

def TestAlpakaHostDeviceCompare(*args, **kwargs):
  mod = cms.EDAnalyzer('TestAlpakaHostDeviceCompare',
    srcHost = cms.required.untracked.InputTag,
    srcDevice = cms.required.untracked.InputTag,
    expectedXdiff = cms.untracked.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
