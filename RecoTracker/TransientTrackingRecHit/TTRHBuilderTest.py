import FWCore.ParameterSet.Config as cms

def TTRHBuilderTest(**kwargs):
  mod = cms.EDAnalyzer('TTRHBuilderTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
