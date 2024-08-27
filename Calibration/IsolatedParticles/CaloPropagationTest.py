import FWCore.ParameterSet.Config as cms

def CaloPropagationTest(**kwargs):
  mod = cms.EDAnalyzer('CaloPropagationTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
