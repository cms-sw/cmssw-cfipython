import FWCore.ParameterSet.Config as cms

def JetImpactParameters(*args, **kwargs):
  mod = cms.EDProducer('JetImpactParameters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
