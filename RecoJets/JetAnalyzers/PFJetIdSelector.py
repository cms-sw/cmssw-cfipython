import FWCore.ParameterSet.Config as cms

def PFJetIdSelector(**kwargs):
  mod = cms.EDProducer('PFJetIdSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
