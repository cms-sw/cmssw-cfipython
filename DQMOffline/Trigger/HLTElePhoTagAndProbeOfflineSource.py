import FWCore.ParameterSet.Config as cms

def HLTElePhoTagAndProbeOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTElePhoTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
