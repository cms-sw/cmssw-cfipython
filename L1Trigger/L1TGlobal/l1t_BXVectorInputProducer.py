import FWCore.ParameterSet.Config as cms

def l1t_BXVectorInputProducer(**kwargs):
  mod = cms.EDProducer('l1t::BXVectorInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
