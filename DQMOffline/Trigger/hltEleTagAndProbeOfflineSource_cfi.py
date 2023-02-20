import FWCore.ParameterSet.Config as cms

hltEleTagAndProbeOfflineSource = cms.EDProducer('HLTEleTagAndProbeOfflineSource',
  tagAndProbeCollections = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
