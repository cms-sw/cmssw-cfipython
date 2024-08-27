import FWCore.ParameterSet.Config as cms

def QcdLowPtDQM(**kwargs):
  mod = cms.EDProducer('QcdLowPtDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
