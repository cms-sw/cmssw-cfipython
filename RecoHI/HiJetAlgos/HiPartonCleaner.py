import FWCore.ParameterSet.Config as cms

def HiPartonCleaner(**kwargs):
  mod = cms.EDProducer('HiPartonCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
