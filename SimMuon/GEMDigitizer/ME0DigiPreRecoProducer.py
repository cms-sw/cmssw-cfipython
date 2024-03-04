import FWCore.ParameterSet.Config as cms

def ME0DigiPreRecoProducer(**kwargs):
  mod = cms.EDProducer('ME0DigiPreRecoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
