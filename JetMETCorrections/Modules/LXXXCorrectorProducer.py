import FWCore.ParameterSet.Config as cms

def LXXXCorrectorProducer(*args, **kwargs):
  mod = cms.EDProducer('LXXXCorrectorProducer',
    level = cms.string(''),
    algorithm = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
