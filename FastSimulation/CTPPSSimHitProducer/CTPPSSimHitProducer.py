import FWCore.ParameterSet.Config as cms

def CTPPSSimHitProducer(*args, **kwargs):
  mod = cms.EDProducer('CTPPSSimHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
