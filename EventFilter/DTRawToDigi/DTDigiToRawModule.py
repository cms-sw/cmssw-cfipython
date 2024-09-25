import FWCore.ParameterSet.Config as cms

def DTDigiToRawModule(*args, **kwargs):
  mod = cms.EDProducer('DTDigiToRawModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
