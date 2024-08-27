import FWCore.ParameterSet.Config as cms

def PatVertexAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatVertexAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
