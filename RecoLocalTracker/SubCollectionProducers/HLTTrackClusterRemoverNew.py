import FWCore.ParameterSet.Config as cms

def HLTTrackClusterRemoverNew(**kwargs):
  mod = cms.EDProducer('HLTTrackClusterRemoverNew',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
