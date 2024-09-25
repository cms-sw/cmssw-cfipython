import FWCore.ParameterSet.Config as cms

def HLTMuTagAndProbeOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTMuTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
