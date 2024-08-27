import FWCore.ParameterSet.Config as cms

def DeepCMVATagInfoProducer(**kwargs):
  mod = cms.EDProducer('DeepCMVATagInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
