import FWCore.ParameterSet.Config as cms

def SteppingHelixPropagatorAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SteppingHelixPropagatorAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
