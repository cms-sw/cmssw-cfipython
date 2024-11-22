import FWCore.ParameterSet.Config as cms

def ESTimingTask(*args, **kwargs):
  mod = cms.EDProducer('ESTimingTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
