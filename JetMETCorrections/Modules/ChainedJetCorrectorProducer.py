import FWCore.ParameterSet.Config as cms

def ChainedJetCorrectorProducer(**kwargs):
  mod = cms.EDProducer('ChainedJetCorrectorProducer',
    correctors = cms.required.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
