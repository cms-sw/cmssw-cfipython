import FWCore.ParameterSet.Config as cms

def ESPedestalTask(*args, **kwargs):
  mod = cms.EDProducer('ESPedestalTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
