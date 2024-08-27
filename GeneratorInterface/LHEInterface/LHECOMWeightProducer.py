import FWCore.ParameterSet.Config as cms

def LHECOMWeightProducer(**kwargs):
  mod = cms.EDProducer('LHECOMWeightProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
