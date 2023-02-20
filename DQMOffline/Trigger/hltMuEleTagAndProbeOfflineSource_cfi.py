import FWCore.ParameterSet.Config as cms

hltMuEleTagAndProbeOfflineSource = cms.EDProducer('HLTMuEleTagAndProbeOfflineSource',
  tagAndProbeCollections = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
