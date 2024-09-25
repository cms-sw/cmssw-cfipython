import FWCore.ParameterSet.Config as cms

def DQMGenericClient(*args, **kwargs):
  mod = cms.EDProducer('DQMGenericClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
