import FWCore.ParameterSet.Config as cms

def CalibratedDigis(**kwargs):
  mod = cms.EDProducer('CalibratedDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
