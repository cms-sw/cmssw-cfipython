import FWCore.ParameterSet.Config as cms

def l1t_GenToInputProducer(**kwargs):
  mod = cms.EDProducer('l1t::GenToInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
