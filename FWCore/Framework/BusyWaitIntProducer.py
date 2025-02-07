import FWCore.ParameterSet.Config as cms

def BusyWaitIntProducer(*args, **kwargs):
  mod = cms.EDProducer('BusyWaitIntProducer',
    ivalue = cms.required.int32,
    iterations = cms.required.uint32,
    lumiNumberToThrow = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
