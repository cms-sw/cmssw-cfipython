import FWCore.ParameterSet.Config as cms

def HTXSRivetProducer(*args, **kwargs):
  mod = cms.EDProducer('HTXSRivetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
