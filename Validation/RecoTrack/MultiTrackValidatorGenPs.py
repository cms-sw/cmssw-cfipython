import FWCore.ParameterSet.Config as cms

def MultiTrackValidatorGenPs(*args, **kwargs):
  mod = cms.EDProducer('MultiTrackValidatorGenPs',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
