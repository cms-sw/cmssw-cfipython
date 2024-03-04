import FWCore.ParameterSet.Config as cms

def ModifiedPhotonProducer(**kwargs):
  mod = cms.EDProducer('ModifiedPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
