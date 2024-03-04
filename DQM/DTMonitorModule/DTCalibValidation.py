import FWCore.ParameterSet.Config as cms

def DTCalibValidation(**kwargs):
  mod = cms.EDProducer('DTCalibValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
