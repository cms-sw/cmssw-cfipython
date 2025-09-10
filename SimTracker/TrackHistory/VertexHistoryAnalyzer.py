import FWCore.ParameterSet.Config as cms

def VertexHistoryAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('VertexHistoryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
