import FWCore.ParameterSet.Config as cms

def TotemTimingDQMSource(**kwargs):
  mod = cms.EDProducer('TotemTimingDQMSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
