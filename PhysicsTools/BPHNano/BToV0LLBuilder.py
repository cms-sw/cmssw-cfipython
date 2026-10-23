import FWCore.ParameterSet.Config as cms

def BToV0LLBuilder(*args, **kwargs):
  mod = cms.EDProducer('BToV0LLBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
