import FWCore.ParameterSet.Config as cms

def PFTauFwdPtrProducer(*args, **kwargs):
  mod = cms.EDProducer('PFTauFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
