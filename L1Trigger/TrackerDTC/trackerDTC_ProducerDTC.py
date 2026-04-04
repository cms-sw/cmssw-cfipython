import FWCore.ParameterSet.Config as cms

def trackerDTC_ProducerDTC(*args, **kwargs):
  mod = cms.EDProducer('trackerDTC::ProducerDTC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
