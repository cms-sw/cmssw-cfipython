import FWCore.ParameterSet.Config as cms

hltElePhoTagAndProbeOfflineSource = cms.EDProducer('HLTElePhoTagAndProbeOfflineSource',
  tagAndProbeCollections = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
