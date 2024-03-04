import FWCore.ParameterSet.Config as cms

def MassKinFitterCandCustomProducer(**kwargs):
  mod = cms.EDProducer('MassKinFitterCandCustomProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
