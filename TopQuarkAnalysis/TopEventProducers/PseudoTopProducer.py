import FWCore.ParameterSet.Config as cms

def PseudoTopProducer(**kwargs):
  mod = cms.EDProducer('PseudoTopProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
