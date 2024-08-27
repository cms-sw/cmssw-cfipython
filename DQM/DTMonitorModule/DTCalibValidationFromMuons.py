import FWCore.ParameterSet.Config as cms

def DTCalibValidationFromMuons(**kwargs):
  mod = cms.EDProducer('DTCalibValidationFromMuons',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
