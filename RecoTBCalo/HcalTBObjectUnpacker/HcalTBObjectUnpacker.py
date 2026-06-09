import FWCore.ParameterSet.Config as cms

def HcalTBObjectUnpacker(*args, **kwargs):
  mod = cms.EDProducer('HcalTBObjectUnpacker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
