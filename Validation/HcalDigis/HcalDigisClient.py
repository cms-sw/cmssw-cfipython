import FWCore.ParameterSet.Config as cms

def HcalDigisClient(*args, **kwargs):
  mod = cms.EDProducer('HcalDigisClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
