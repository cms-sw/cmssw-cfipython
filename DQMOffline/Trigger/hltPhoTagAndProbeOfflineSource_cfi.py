import FWCore.ParameterSet.Config as cms

hltPhoTagAndProbeOfflineSource = cms.EDProducer('HLTPhoTagAndProbeOfflineSource',
  tagAndProbeCollections = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
