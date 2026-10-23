import FWCore.ParameterSet.Config as cms

def TrackAssociatorByChi2Producer(*args, **kwargs):
  mod = cms.EDProducer('TrackAssociatorByChi2Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
