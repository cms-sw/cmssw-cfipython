import FWCore.ParameterSet.Config as cms

def B2GDoubleLeptonHLTValidation(*args, **kwargs):
  mod = cms.EDProducer('B2GDoubleLeptonHLTValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
