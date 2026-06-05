import FWCore.ParameterSet.Config as cms

def DTDigiTask(*args, **kwargs):
  mod = cms.EDProducer('DTDigiTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
