import FWCore.ParameterSet.Config as cms

def RecHitFilter(**kwargs):
  mod = cms.EDProducer('RecHitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
