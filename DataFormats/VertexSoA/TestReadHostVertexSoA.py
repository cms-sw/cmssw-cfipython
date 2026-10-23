import FWCore.ParameterSet.Config as cms

def TestReadHostVertexSoA(*args, **kwargs):
  mod = cms.EDAnalyzer('TestReadHostVertexSoA',
    input = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
