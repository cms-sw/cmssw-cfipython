import FWCore.ParameterSet.Config as cms

def HiSpikeCleaner(**kwargs):
  mod = cms.EDProducer('HiSpikeCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
