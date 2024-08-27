import FWCore.ParameterSet.Config as cms

def DeepFlavourJetTagsProducer(**kwargs):
  mod = cms.EDProducer('DeepFlavourJetTagsProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
