import FWCore.ParameterSet.Config as cms

def CentralitypADQM(**kwargs):
  mod = cms.EDProducer('CentralitypADQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
