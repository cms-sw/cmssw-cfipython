import FWCore.ParameterSet.Config as cms

def HLTEleTagAndProbeOfflineSource(**kwargs):
  mod = cms.EDProducer('HLTEleTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
