import FWCore.ParameterSet.Config as cms

def AlcaPCCIntegrator(*args, **kwargs):
  mod = cms.EDProducer('AlcaPCCIntegrator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
