import FWCore.ParameterSet.Config as cms

def DTCalibValidation(*args, **kwargs):
  mod = cms.EDProducer('DTCalibValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
