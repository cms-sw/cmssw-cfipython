import FWCore.ParameterSet.Config as cms

def BusyWaitIntOneSharedProducer(*args, **kwargs):
  mod = cms.EDProducer('BusyWaitIntOneSharedProducer',
    ivalue = cms.required.int32,
    iterations = cms.required.uint32,
    resourceNames = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
