import FWCore.ParameterSet.Config as cms

def TrackProducerWithSCAssociation(*args, **kwargs):
  mod = cms.EDProducer('TrackProducerWithSCAssociation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
