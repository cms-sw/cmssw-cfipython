import FWCore.ParameterSet.Config as cms

def CSCHaloDataProducer(*args, **kwargs):
  mod = cms.EDProducer('CSCHaloDataProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
