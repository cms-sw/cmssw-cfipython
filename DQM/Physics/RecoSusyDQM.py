import FWCore.ParameterSet.Config as cms

def RecoSusyDQM(*args, **kwargs):
  mod = cms.EDProducer('RecoSusyDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
