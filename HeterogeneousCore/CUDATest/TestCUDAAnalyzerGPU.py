import FWCore.ParameterSet.Config as cms

def TestCUDAAnalyzerGPU(*args, **kwargs):
  mod = cms.EDAnalyzer('TestCUDAAnalyzerGPU',
    src = cms.InputTag(''),
    minValue = cms.double(-1e+308),
    maxValue = cms.double(1e+308),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
