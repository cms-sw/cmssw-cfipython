import FWCore.ParameterSet.Config as cms

def PrimaryVertexAnalyzer4PUSlimmed(*args, **kwargs):
  mod = cms.EDProducer('PrimaryVertexAnalyzer4PUSlimmed',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
