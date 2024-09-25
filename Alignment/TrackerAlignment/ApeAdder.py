import FWCore.ParameterSet.Config as cms

def ApeAdder(*args, **kwargs):
  mod = cms.EDAnalyzer('ApeAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
