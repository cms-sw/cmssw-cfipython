import FWCore.ParameterSet.Config as cms

def SteppingHelixPropagatorAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SteppingHelixPropagatorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
