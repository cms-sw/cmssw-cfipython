import FWCore.ParameterSet.Config as cms

def PFTauFwdPtrProducer(**kwargs):
  mod = cms.EDProducer('PFTauFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
