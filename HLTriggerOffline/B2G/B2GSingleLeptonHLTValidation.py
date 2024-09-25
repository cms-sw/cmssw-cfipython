import FWCore.ParameterSet.Config as cms

def B2GSingleLeptonHLTValidation(*args, **kwargs):
  mod = cms.EDProducer('B2GSingleLeptonHLTValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
