import FWCore.ParameterSet.Config as cms

def IsolationExample(*args, **kwargs):
  mod = cms.EDAnalyzer('IsolationExample',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
