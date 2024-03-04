import FWCore.ParameterSet.Config as cms

def CaloJetIdSelector(**kwargs):
  mod = cms.EDProducer('CaloJetIdSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
