import FWCore.ParameterSet.Config as cms

def TestCUDAAnalyzerGPU(**kwargs):
  mod = cms.EDAnalyzer('TestCUDAAnalyzerGPU',
    src = cms.InputTag(''),
    minValue = cms.double(-1e+308),
    maxValue = cms.double(1e+308),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
