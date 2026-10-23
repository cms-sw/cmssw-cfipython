import FWCore.ParameterSet.Config as cms

def NjettinessAdder(*args, **kwargs):
  mod = cms.EDProducer('NjettinessAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
