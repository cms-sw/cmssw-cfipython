import FWCore.ParameterSet.Config as cms

def GenJetIdSelector(**kwargs):
  mod = cms.EDProducer('GenJetIdSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
