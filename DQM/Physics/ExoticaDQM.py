import FWCore.ParameterSet.Config as cms

def ExoticaDQM(*args, **kwargs):
  mod = cms.EDProducer('ExoticaDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
