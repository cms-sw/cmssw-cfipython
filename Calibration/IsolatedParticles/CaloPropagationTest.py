import FWCore.ParameterSet.Config as cms

def CaloPropagationTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloPropagationTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
