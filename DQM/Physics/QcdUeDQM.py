import FWCore.ParameterSet.Config as cms

def QcdUeDQM(*args, **kwargs):
  mod = cms.EDProducer('QcdUeDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
