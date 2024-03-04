import FWCore.ParameterSet.Config as cms

def DSVProducer(**kwargs):
  mod = cms.EDProducer('DSVProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
