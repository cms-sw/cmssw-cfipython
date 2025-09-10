import FWCore.ParameterSet.Config as cms

def CalibratedDigis(*args, **kwargs):
  mod = cms.EDProducer('CalibratedDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
