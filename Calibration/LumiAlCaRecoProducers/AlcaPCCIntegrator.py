import FWCore.ParameterSet.Config as cms

def AlcaPCCIntegrator(**kwargs):
  mod = cms.EDProducer('AlcaPCCIntegrator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
