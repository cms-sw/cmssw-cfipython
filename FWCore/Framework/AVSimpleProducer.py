import FWCore.ParameterSet.Config as cms

def AVSimpleProducer(**kwargs):
  mod = cms.EDProducer('AVSimpleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
