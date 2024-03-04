import FWCore.ParameterSet.Config as cms

def ConvertedPhotonProducer(**kwargs):
  mod = cms.EDProducer('ConvertedPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
