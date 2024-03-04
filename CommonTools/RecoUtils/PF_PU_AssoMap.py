import FWCore.ParameterSet.Config as cms

def PF_PU_AssoMap(**kwargs):
  mod = cms.EDProducer('PF_PU_AssoMap',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
