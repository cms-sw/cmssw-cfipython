import FWCore.ParameterSet.Config as cms

def ZCounting(*args, **kwargs):
  mod = cms.EDProducer('ZCounting',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
