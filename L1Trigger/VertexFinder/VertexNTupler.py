import FWCore.ParameterSet.Config as cms

def VertexNTupler(**kwargs):
  mod = cms.EDAnalyzer('VertexNTupler',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
