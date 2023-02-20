import FWCore.ParameterSet.Config as cms

hltMuPhoTagAndProbeOfflineSource = cms.EDProducer('HLTMuPhoTagAndProbeOfflineSource',
  tagAndProbeCollections = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
