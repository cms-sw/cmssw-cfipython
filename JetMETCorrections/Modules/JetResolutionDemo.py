import FWCore.ParameterSet.Config as cms

def JetResolutionDemo(*args, **kwargs):
  mod = cms.EDAnalyzer('JetResolutionDemo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
