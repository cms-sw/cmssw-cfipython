import FWCore.ParameterSet.Config as cms

def PatBJetVertexAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatBJetVertexAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
