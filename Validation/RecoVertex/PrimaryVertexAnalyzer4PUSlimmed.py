import FWCore.ParameterSet.Config as cms

def PrimaryVertexAnalyzer4PUSlimmed(**kwargs):
  mod = cms.EDProducer('PrimaryVertexAnalyzer4PUSlimmed',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
