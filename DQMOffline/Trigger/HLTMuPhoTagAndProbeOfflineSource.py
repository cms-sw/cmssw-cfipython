import FWCore.ParameterSet.Config as cms

def HLTMuPhoTagAndProbeOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTMuPhoTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
