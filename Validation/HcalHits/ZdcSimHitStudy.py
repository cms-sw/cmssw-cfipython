import FWCore.ParameterSet.Config as cms

def ZdcSimHitStudy(*args, **kwargs):
  mod = cms.EDProducer('ZdcSimHitStudy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
