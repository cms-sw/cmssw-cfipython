import FWCore.ParameterSet.Config as cms

def HLTPhoTagAndProbeOfflineSource(**kwargs):
  mod = cms.EDProducer('HLTPhoTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
