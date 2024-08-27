import FWCore.ParameterSet.Config as cms

def VtxTester(**kwargs):
  mod = cms.EDAnalyzer('VtxTester',
    src = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
