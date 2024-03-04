import FWCore.ParameterSet.Config as cms

def TestAlpakaHostDeviceCompare(**kwargs):
  mod = cms.EDAnalyzer('TestAlpakaHostDeviceCompare',
    srcHost = cms.required.untracked.InputTag,
    srcDevice = cms.required.untracked.InputTag,
    expectedXdiff = cms.untracked.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
