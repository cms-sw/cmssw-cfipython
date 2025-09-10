import FWCore.ParameterSet.Config as cms

def BToTrkLLBuilder(*args, **kwargs):
  mod = cms.EDProducer('BToTrkLLBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
