import FWCore.ParameterSet.Config as cms

hltMuTagAndProbeOfflineSource = cms.EDProducer('HLTMuTagAndProbeOfflineSource',
  tagAndProbeCollections = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
