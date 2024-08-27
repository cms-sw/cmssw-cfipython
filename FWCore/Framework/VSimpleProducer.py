import FWCore.ParameterSet.Config as cms

def VSimpleProducer(**kwargs):
  mod = cms.EDProducer('VSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
