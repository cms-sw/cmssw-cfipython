import FWCore.ParameterSet.Config as cms

def PATHeavyIonProducer(**kwargs):
  mod = cms.EDProducer('PATHeavyIonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
