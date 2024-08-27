import FWCore.ParameterSet.Config as cms

def HLTElePhoTagAndProbeOfflineSource(**kwargs):
  mod = cms.EDProducer('HLTElePhoTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
