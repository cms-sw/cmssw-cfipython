import FWCore.ParameterSet.Config as cms

def MultiTrackValidatorGenPs(**kwargs):
  mod = cms.EDProducer('MultiTrackValidatorGenPs',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
