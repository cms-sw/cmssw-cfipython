import FWCore.ParameterSet.Config as cms

def TotemTimingDQMSource(*args, **kwargs):
  mod = cms.EDProducer('TotemTimingDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
