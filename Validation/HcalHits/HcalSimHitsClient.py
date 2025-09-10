import FWCore.ParameterSet.Config as cms

def HcalSimHitsClient(*args, **kwargs):
  mod = cms.EDProducer('HcalSimHitsClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
