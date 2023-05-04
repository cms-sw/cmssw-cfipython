import FWCore.ParameterSet.Config as cms

testAlpakaHostDeviceCompare = cms.EDAnalyzer('TestAlpakaHostDeviceCompare',
  srcHost = cms.required.untracked.InputTag,
  srcDevice = cms.required.untracked.InputTag,
  expectedXdiff = cms.untracked.double(0),
  mightGet = cms.optional.untracked.vstring
)
