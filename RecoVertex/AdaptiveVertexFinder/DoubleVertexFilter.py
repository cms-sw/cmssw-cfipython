import FWCore.ParameterSet.Config as cms

def DoubleVertexFilter(**kwargs):
  mod = cms.EDProducer('DoubleVertexFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
