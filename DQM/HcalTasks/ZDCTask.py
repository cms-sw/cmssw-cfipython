import FWCore.ParameterSet.Config as cms

def ZDCTask(*args, **kwargs):
  mod = cms.EDProducer('ZDCTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
