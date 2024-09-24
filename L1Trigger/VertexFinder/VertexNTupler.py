import FWCore.ParameterSet.Config as cms

def VertexNTupler(*args, **kwargs):
  mod = cms.EDAnalyzer('VertexNTupler',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
