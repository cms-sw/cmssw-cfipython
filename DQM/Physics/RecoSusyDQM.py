import FWCore.ParameterSet.Config as cms

def RecoSusyDQM(**kwargs):
  mod = cms.EDProducer('RecoSusyDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
