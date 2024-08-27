import FWCore.ParameterSet.Config as cms

def PatBJetVertexAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PatBJetVertexAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
