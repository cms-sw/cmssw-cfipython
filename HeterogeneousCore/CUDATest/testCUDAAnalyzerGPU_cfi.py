import FWCore.ParameterSet.Config as cms

testCUDAAnalyzerGPU = cms.EDAnalyzer('TestCUDAAnalyzerGPU',
  src = cms.InputTag(''),
  minValue = cms.double(-1e+308),
  maxValue = cms.double(1e+308),
  mightGet = cms.optional.untracked.vstring
)
