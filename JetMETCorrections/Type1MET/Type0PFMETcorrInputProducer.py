import FWCore.ParameterSet.Config as cms

def Type0PFMETcorrInputProducer(*args, **kwargs):
  mod = cms.EDProducer('Type0PFMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
