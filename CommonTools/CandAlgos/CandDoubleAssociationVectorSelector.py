import FWCore.ParameterSet.Config as cms

def CandDoubleAssociationVectorSelector(*args, **kwargs):
  mod = cms.EDProducer('CandDoubleAssociationVectorSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
