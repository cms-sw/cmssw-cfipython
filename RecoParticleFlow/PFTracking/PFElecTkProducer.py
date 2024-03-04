import FWCore.ParameterSet.Config as cms

def PFElecTkProducer(**kwargs):
  mod = cms.EDProducer('PFElecTkProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
