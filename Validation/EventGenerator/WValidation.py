import FWCore.ParameterSet.Config as cms

def WValidation(**kwargs):
  mod = cms.EDProducer('WValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
