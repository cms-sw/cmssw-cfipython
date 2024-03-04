import FWCore.ParameterSet.Config as cms

def EcalTBMCInfoProducer(**kwargs):
  mod = cms.EDProducer('EcalTBMCInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
