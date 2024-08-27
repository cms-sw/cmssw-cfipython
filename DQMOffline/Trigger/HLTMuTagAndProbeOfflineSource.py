import FWCore.ParameterSet.Config as cms

def HLTMuTagAndProbeOfflineSource(**kwargs):
  mod = cms.EDProducer('HLTMuTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
