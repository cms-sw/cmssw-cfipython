import FWCore.ParameterSet.Config as cms

def l1t_GenToInputProducer(*args, **kwargs):
  mod = cms.EDProducer('l1t::GenToInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
