import FWCore.ParameterSet.Config as cms

def CandDoubleAssociationVector2ValueMap(*args, **kwargs):
  mod = cms.EDProducer('CandDoubleAssociationVector2ValueMap',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
