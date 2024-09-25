import FWCore.ParameterSet.Config as cms

def CSCTriggerPrimitivesProducer(*args, **kwargs):
  mod = cms.EDProducer('CSCTriggerPrimitivesProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
