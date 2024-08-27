import FWCore.ParameterSet.Config as cms

def CandDoubleAssociationVector2ValueMap(**kwargs):
  mod = cms.EDProducer('CandDoubleAssociationVector2ValueMap',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
