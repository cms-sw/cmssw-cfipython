import FWCore.ParameterSet.Config as cms

def HLTTrackClusterRemoverNew(*args, **kwargs):
  mod = cms.EDProducer('HLTTrackClusterRemoverNew',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
