import FWCore.ParameterSet.Config as cms

def BusyWaitIntOneSharedProducer(**kwargs):
  mod = cms.EDProducer('BusyWaitIntOneSharedProducer',
    ivalue = cms.required.int32,
    iterations = cms.required.uint32,
    resourceNames = cms.untracked.vstring(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
