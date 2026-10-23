import FWCore.ParameterSet.Config as cms

def l1t_BXVectorInputProducer(*args, **kwargs):
  mod = cms.EDProducer('l1t::BXVectorInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
