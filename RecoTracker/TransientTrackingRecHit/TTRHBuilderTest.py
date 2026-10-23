import FWCore.ParameterSet.Config as cms

def TTRHBuilderTest(*args, **kwargs):
  mod = cms.EDAnalyzer('TTRHBuilderTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
