import FWCore.ParameterSet.Config as cms

def EvtPlaneProducer(*args, **kwargs):
  mod = cms.EDProducer('EvtPlaneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
