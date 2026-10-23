import FWCore.ParameterSet.Config as cms

def MonitorLTC(*args, **kwargs):
  mod = cms.EDProducer('MonitorLTC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
