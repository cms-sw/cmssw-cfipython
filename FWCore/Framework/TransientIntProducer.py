import FWCore.ParameterSet.Config as cms

def TransientIntProducer(**kwargs):
  mod = cms.EDProducer('TransientIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
