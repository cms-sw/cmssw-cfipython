import FWCore.ParameterSet.Config as cms

def JetFlavourIdentifier(**kwargs):
  mod = cms.EDProducer('JetFlavourIdentifier',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
