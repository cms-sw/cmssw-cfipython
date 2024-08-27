import FWCore.ParameterSet.Config as cms

def PFJetToCaloProducer(**kwargs):
  mod = cms.EDProducer('PFJetToCaloProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
