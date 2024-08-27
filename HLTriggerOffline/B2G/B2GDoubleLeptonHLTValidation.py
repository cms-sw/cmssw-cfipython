import FWCore.ParameterSet.Config as cms

def B2GDoubleLeptonHLTValidation(**kwargs):
  mod = cms.EDProducer('B2GDoubleLeptonHLTValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
