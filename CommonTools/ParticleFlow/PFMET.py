import FWCore.ParameterSet.Config as cms

def PFMET(**kwargs):
  mod = cms.EDProducer('PFMET',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
