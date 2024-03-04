import FWCore.ParameterSet.Config as cms

def PFCand_AssoMap(**kwargs):
  mod = cms.EDProducer('PFCand_AssoMap',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
