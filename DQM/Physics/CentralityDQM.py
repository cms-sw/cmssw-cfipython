import FWCore.ParameterSet.Config as cms

def CentralityDQM(**kwargs):
  mod = cms.EDProducer('CentralityDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
