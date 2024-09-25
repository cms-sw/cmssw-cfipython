import FWCore.ParameterSet.Config as cms

def HLTMuEleTagAndProbeOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTMuEleTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
