import FWCore.ParameterSet.Config as cms

def DTTrigTest(**kwargs):
  mod = cms.EDAnalyzer('DTTrigTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
