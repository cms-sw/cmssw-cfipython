import FWCore.ParameterSet.Config as cms

def CandDoubleAssociationVectorSelector(**kwargs):
  mod = cms.EDProducer('CandDoubleAssociationVectorSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
