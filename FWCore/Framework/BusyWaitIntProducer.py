import FWCore.ParameterSet.Config as cms

def BusyWaitIntProducer(**kwargs):
  mod = cms.EDProducer('BusyWaitIntProducer',
    ivalue = cms.required.int32,
    iterations = cms.required.uint32,
    lumiNumberToThrow = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
