import FWCore.ParameterSet.Config as cms

def PatVertexAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatVertexAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
