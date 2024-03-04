import FWCore.ParameterSet.Config as cms

def OVSimpleProducer(**kwargs):
  mod = cms.EDProducer('OVSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
