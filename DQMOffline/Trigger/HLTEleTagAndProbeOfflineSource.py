import FWCore.ParameterSet.Config as cms

def HLTEleTagAndProbeOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTEleTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
