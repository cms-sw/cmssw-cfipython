import FWCore.ParameterSet.Config as cms

def PFNuclearProducer(**kwargs):
  mod = cms.EDProducer('PFNuclearProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
