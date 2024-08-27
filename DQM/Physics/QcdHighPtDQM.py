import FWCore.ParameterSet.Config as cms

def QcdHighPtDQM(**kwargs):
  mod = cms.EDProducer('QcdHighPtDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
