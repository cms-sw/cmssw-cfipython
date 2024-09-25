import FWCore.ParameterSet.Config as cms

def MonitorTrackResiduals(*args, **kwargs):
  mod = cms.EDProducer('MonitorTrackResiduals',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
