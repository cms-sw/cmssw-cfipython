import FWCore.ParameterSet.Config as cms

def l1t_FakeInputProducer(**kwargs):
  mod = cms.EDProducer('l1t::FakeInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
