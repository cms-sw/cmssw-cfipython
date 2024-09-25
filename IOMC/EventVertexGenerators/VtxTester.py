import FWCore.ParameterSet.Config as cms

def VtxTester(*args, **kwargs):
  mod = cms.EDAnalyzer('VtxTester',
    src = cms.InputTag('generatorSmeared'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
