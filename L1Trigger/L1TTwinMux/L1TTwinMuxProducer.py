import FWCore.ParameterSet.Config as cms

def L1TTwinMuxProducer(**kwargs):
  mod = cms.EDProducer('L1TTwinMuxProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
