import FWCore.ParameterSet.Config as cms

def trackerDTC_ProducerED(*args, **kwargs):
  mod = cms.EDProducer('trackerDTC::ProducerED',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
