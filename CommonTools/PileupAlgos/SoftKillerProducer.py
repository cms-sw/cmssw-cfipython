import FWCore.ParameterSet.Config as cms

def SoftKillerProducer(**kwargs):
  mod = cms.EDProducer('SoftKillerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
