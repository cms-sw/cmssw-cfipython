import FWCore.ParameterSet.Config as cms

def HLTVertexPerformanceAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('HLTVertexPerformanceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
