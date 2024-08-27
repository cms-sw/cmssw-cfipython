import FWCore.ParameterSet.Config as cms

def VertexHistoryAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('VertexHistoryAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
