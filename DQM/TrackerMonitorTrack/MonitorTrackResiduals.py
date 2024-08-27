import FWCore.ParameterSet.Config as cms

def MonitorTrackResiduals(**kwargs):
  mod = cms.EDProducer('MonitorTrackResiduals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
